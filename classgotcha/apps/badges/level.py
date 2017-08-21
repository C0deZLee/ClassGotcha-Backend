from django.shortcuts import get_object_or_404

from models import Action


def init_actions():
	Action.objects.bulk_create([
		Action(name='verify_email', exp=50),
		Action(name='update_user_info', exp=25),
		Action(name='refer_friend', exp=25),

		# Classrooms
		Action(name='update_classroom_info', exp=10),
		Action(name='add_classroom', exp=10),
		Action(name='add_friend', exp=5),

		# File Uploads
		Action(name='upload_file', exp=10),
		Action(name='confirm_file', exp=5),

		# Tasks
		Action(name='set_task', exp=5),
		Action(name='confirm_task', exp=5),

		# Posts
		Action(name='post', exp=1),

		## Questions
		Action(name='post_question', exp=5),
		Action(name='question_upvoted', exp=2),
		Action(name='question_downvoted', exp=-1),
		Action(name='answer_question', exp=0),
		Action(name='answer_upvoted', exp=4),
		Action(name='answer_downvoted', exp=-2),

		# Reports
		Action(name='report_bug', exp=5),
		Action(name='report_issue', exp=5),
	])
	pass


def level_up(account, exp):
	# this is how we calculate exp for each level
	level_up_exp = int(2.5 ** (account.level-1) * 10) * 10
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
