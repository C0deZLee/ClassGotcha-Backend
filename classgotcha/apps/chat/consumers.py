import re, json, logging

from django.core.exceptions import ObjectDoesNotExist

from channels import Group
from channels.sessions import channel_session
from classgotcha.apps.chat.models import Room
from classgotcha.apps.chat.scripts.Conversation import run, Backendhandler

log = logging.getLogger(__name__)


@channel_session
def ws_disconnect(message):
	try:
		pk = message.channel_session['room']
		room = Room.objects.get(pk=pk)
		Group('chat-' + str(pk), channel_layer=message.channel_layer).discard(message.reply_channel)
	except (KeyError, Room.DoesNotExist):
		pass


@channel_session
def ws_connect(message):
	# Extract the room from the message. This expects message.path to be of the
	# form /chat/{label}/, and finds a Room if the message path is applicable,
	# and if the Room exists. Otherwise, bails (meaning this is a some othersort
	# of websocket). So, this is effectively a version of _get_object_or_404.
	try:
		print message['path']
		prefix, pk = message['path'].decode('ascii').strip('/').split('/')
		if prefix != 'chat':
			log.debug('invalid ws path=%s', message['path'])
			return
		room = Room.objects.get(pk=pk)
	except ValueError:
		print 'invalid ws path=' + message['path']
		log.debug('invalid ws path=%s', message['path'])
		ws_disconnect(message)
		return
	except ObjectDoesNotExist:
		print 'ws room does not exist pk=' + pk
		log.debug('ws room does not exist pk=%s', pk)
		ws_disconnect(message)
		return
	print ('chat connect room=%s client=%s:%s',
	       room.pk, message['client'][0], message['client'][1])
	log.debug('chat connect room=%s client=%s:%s',
	          room.pk, message['client'][0], message['client'][1])

	# Need to be explicit about the channel layer so that testability works
	# This may be a FIXME?
	Group('chat-' + str(pk), channel_layer=message.channel_layer).add(message.reply_channel)
	# Create room id in channel session
	message.channel_session['room'] = room.pk


@channel_session
def ws_receive(message):
	# Look up the room from the channel session, bailing if it doesn't exist
	print "receive"
	try:
		pk = message.channel_session['room']
		room = Room.objects.get(pk=pk)
	except KeyError:
		print 'no room in channel_session'
		log.debug('no room in channel_session')
		return
	except Room.DoesNotExist:
		print 'recieved message, buy room does not exist pk=' + pk
		log.debug('recieved message, buy room does not exist pk=%s', pk)
		return

	# Parse out a chat message from the content text, bailing if it doesn't
	# conform to the expected message format.
	try:
		data = json.loads(message['text'])
		print data
	except ValueError:
		log.debug("ws message isn't json text=%s", message['text'])
		return

	if set(data.keys()) != set(('username', 'message')):
		log.debug("ws message unexpected format data=%s", data)
		return

	if data:
		log.debug('chat message room=%s username=%s message=%s',
		          room.pk, data['username'], data['message'])

		user_name = data.get('username', 'robot')

		m = room.messages.create(**data)
		Group('chat-' + str(pk), channel_layer=message.channel_layer).send({'text': json.dumps(m.as_dict())})

		# ------------------------- IBM ------------------------
		# try:
		# 	context = json.loads(room.messages.latest().context)
		# except:
		# 	context = None
		# response = json.loads(json.dumps(run(message=data['message'], context=context)))
		# # print response
		# response_text = response['output']['text'][0]
		# context = json.loads(json.dumps(response['context']))
		# try:
		# 	# node = json.loads(json.dumps(response['context']['system']['dialog_stack'][-1]['dialog_node']))
		# 	node = json.loads(json.dumps(response['output']['nodes_visited'][-1]))
		# 	print node
		# except:
		# 	node = "root"
		#
		# try:
		# 	intent = []
		# 	for i in range(0, len(response['intents'])):
		# 		intent.append(json.loads(json.dumps(response['intents'][i]['intent'])))
		# except:
		# 	intent = "None"
		# try:
		# 	entity = []
		# 	for i in range(0, len(response['entities'])):
		# 		entity.append(json.loads(json.dumps(response['entities'][i]['value'])))
		# except:
		# 	print "entity bug"
		# 	entity = "None"
		#
		# m1 = room.messages.create(username='robot', message=response_text, context=json.dumps(context))
		# try:
		# 	toreturn = Backendhandler(user_name, intent, entity, node)
		# 	print toreturn
		# except:
		# 	pass
		#
		# # room.message.create(response)
		#
		# # See above for the note about Group
		#
		# Group('chat-' + str(pk), channel_layer=message.channel_layer).send({'text': json.dumps(m1.as_dict())})
