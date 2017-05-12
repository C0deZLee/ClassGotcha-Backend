from django.shortcuts import get_object_or_404

from models import Action


def init_actions():
	# Action.objects.create()
	pass


def trigger_action(account, action_name):
	action = get_object_or_404(Action.objects.all(), name=action_name)
	account.exp = account.exp + action.exp
	# TODO: how to auto level-up ?
	pass
