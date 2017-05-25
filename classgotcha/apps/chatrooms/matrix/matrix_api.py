import json
import requests
from django.conf import settings
from urllib import quote
from rest_framework import status

# try:
# except ImportError:
# 	from urllib.parse import quote

MATRIX_API_ROOT = '/_matrix/client/r0'
MATRIX_HOST = settings.MATRIX_HOST


class MatrixApi(object):
	def __init__(self, auth_token=None, base_url=MATRIX_HOST, api_root=MATRIX_API_ROOT):
		"""Construct and configure the HTTP API.
		Args:
			base_url(str): Optional. The home server URL. Default is set to settings.MATRIX_HOST
		"""
		self.base_url = base_url
		self.auth_token = auth_token
		self.api_root = api_root

	def _send(self, method, api_path,
	          content=None, query_params=None, headers=None
	          ):
		"""Perform Send HTTP Request
		 Args:
			method(str): Required. 'GET', 'PUT', 'DELETE', 'POST'
			api_path(str): Required. The api path, e.g '/user/{userId}/filter/{filterId}'
			api_root(str): Optional. Default is set to self.api_root
			content(dic): Optional
			query_params(dic): Optional
			headers(dic): Optional
		"""
		method = method.upper()
		if method not in ['GET', 'PUT', 'DELETE', 'POST']:
			print '405 Method not allowed'
			return False

		if headers is None:
			headers = {}

		if query_params is None:
			query_params = {}

		if 'Content-Type' not in headers:
			headers['Content-Type'] = 'application/json'

		if headers['Content-Type'] == 'application/json' and content is not None:
			content = json.dumps(content)

		if self.auth_token:
			query_params['access_token'] = self.auth_token

		query_params['kind'] = 'user'

		endpoint = self.base_url + self.api_root + api_path

		response = requests.request(
			method, endpoint,
			params=query_params,
			data=content,
			headers=headers,
		)

		if response.status_code < 200 or response.status_code >= 300:
			print response.status_code, response.text,
			return False

		return response.json()

	def sync(self, since=None, timeout_ms=30000, filter=None,
	         full_state=None, set_presence=None):
		""" Perform a sync request.

		Args:
			since(str): Optional. A token which specifies where to continue a sync from.
			timeout_ms(int): Optional. The time in milliseconds to wait.
			filter (int|str): Either a Filter ID or a JSON string.
			full_state (bool): Return the full state for every room the user has joined
				Defaults to false.
			set_presence (str): Should the client be marked as 'online' or' offline'
		"""

		request = {
			'timeout': timeout_ms
		}

		if since:
			request['since'] = since

		if filter:
			request['filter'] = filter

		if full_state:
			request['full_state'] = full_state

		if set_presence:
			request['set_presence'] = set_presence

		return self._send('GET', '/sync', query_params=request)

	def register(self, username, password, bind_email=False, auth=None):
		"""Performs /register.
		Args:
			username(str): Required. username
			password(str): Required. password
			bind_email(bool): Optional. Default is false
			auth(dic): Optional.
		"""

		if auth is None:
			auth = {'type'   : 'm.login.dummy',
			        'session': ''}

		content = {'username'  : username,
		           'password'  : password,
		           'bind_email': bind_email,
		           'auth'      : auth}

		response = self._send('POST', '/register', content)

		# if respond with False, means username conflict, however the username in matrix doesn't matter
		while not response:
			content['username'] += '1'
			response = self._send('POST', '/register', content)
		return response

	def create_room(self, name, preset='public_chat', is_public=True, topic=''):
		"""Perform /createRoom.

		Args:
			name(str): Required. Chatroom name
			preset(str): Optional. One of ['private_chat', 'public_chat', 'trusted_private_chat']
				Detail: matrix.org/docs/spec/client_server/latest.html#post-matrix-client-r0-createroom
			is_public(bool): Optional. The public/private visibility.
			topic(str): Optional. Topic of chatrooms.
		"""
		body = {
			'name'      : name,
			'visibility': 'public' if is_public else 'private',
			'preset'    : preset
		}

		if topic:
			body['topic'] = topic

		return self._send('POST', '/createRoom', body)

	def join_room(self, room_id=None):
		"""Performs /join/$room_id

		Args:
			room_id(str): The room ID to join.
		"""
		if not room_id:
			print 'Room Not Found'
			return False

		return self._send('POST', '/join/' + room_id)

	def leave_room(self, room_id=None):
		"""Perform POST /rooms/$room_id/leave
		Args:
			room_id(str): The room ID
		"""
		if not room_id:
			print 'Room Not Found'
			return False

		return self._send('POST', '/rooms/' + room_id + '/leave')
