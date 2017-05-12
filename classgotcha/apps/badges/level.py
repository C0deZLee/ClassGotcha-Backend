from django.shortcuts import get_object_or_404

from models import Action


def init_actions():
	# Action.objects.create()
	pass


def level_up(account, exp):
	# this is how we calculate exp for each level
	level_up_exp = int(2.5**(account.level-1)*10)*10
	account.exp += exp
	if account.exp > level_up_exp:
		account.level += 1
	account.save()
	trigger_action(account, "levelup")
	return


def trigger_action(account, action_name):
	action = get_object_or_404(Action.objects.all(), name=action_name)
	level_up(account, action.exp)
	pass
