from django.db import IntegrityError

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from models import Action, BadgeType


@api_view(['GET'])
@permission_classes((IsAdminUser,))
def action_init(request):
	try:
		Action.objects.bulk_create([
			Action(name='verify_email', exp=50),
			Action(name='update_user_info', exp=25),
			Action(name='refer_friend', exp=25),

			# Classrooms
			Action(name='update_classroom_info', exp=10),
			Action(name='add_classroom', exp=10),
			Action(name='add_friend', exp=5),

			# File Uploads
			Action(name='upload_file', exp=20),

			# Tasks
			Action(name='add_classroom_task', exp=5),
			Action(name='edit_classroom_task', exp=5),

			# Questions
			Action(name='post_normal', exp=1),
			Action(name='reply_normal', exp=1),
			Action(name='post_question', exp=5),
			Action(name='answer_question', exp=5),
			Action(name='answer_approved', exp=15),

			# Reports
			Action(name='report_forum', exp=5),
			Action(name='report_user', exp=5),
			Action(name='report_post', exp=5),
			Action(name='report_classroom_task', exp=5),
		])
	except IntegrityError:
		pass

	try:
		BadgeType.objects.bulk_create([
			BadgeType(name='Email Verified', action_required=1, identifier='Email Verified', description='Email Verification'),

			BadgeType(name='Completed User Information', action_required=1, identifier='Completed User Information', description='User Information'),

			# Friends refer
			BadgeType(name='Friend Referred I', action_required=1, identifier='Friend Referred', description='Refer 1 Friend'),
			BadgeType(name='Friends Referred II', action_required=2, identifier='Friend Referred', level=2, description='Refer 2 Friends'),
			BadgeType(name='Friends Referred III', action_required=5, identifier='Friend Referred', level=3, description='Refer 5 Friends'),

			# Classrooms
			BadgeType(name='Classroom Contributor I', action_required=1, identifier='Classroom Contributor', description='Complete 1 classroom info'),
			BadgeType(name='Classroom Contributor II', action_required=2, identifier='Classroom Contributor', level=2, description='Complete 2 Classroom Info'),
			BadgeType(name='Classroom Contributor III', action_required=5, identifier='Classroom Contributor', level=3, description='Complete 5 Classroom Info'),

			BadgeType(name='Friend I', action_required=1, identifier='Friend', description='Have 1 friend'),
			BadgeType(name='Friend II', action_required=2, identifier='Friend', level=2, description='Have 2 friends'),
			BadgeType(name='Friend III', action_required=5, identifier='Friend', level=3, description='Have 5 friends'),
			BadgeType(name='Friend IV', action_required=10, identifier='Friend', level=3, description='Have 10 friends'),
			BadgeType(name='Friend V', action_required=20, identifier='Friend', level=3, description='Have 20 friends'),

			# File Uploads
			BadgeType(name='Notes Contributor I', action_required=1, identifier='Notes Contributor', description='Contribute 1 Note'),
			BadgeType(name='Notes Contributor II', action_required=2, identifier='Notes Contributor', level=2, description='Contribute 2 Notes'),
			BadgeType(name='Notes Contributor III', action_required=5, identifier='Notes Contributor', level=3, description='Contribute 5 Notes'),
			BadgeType(name='Notes Contributor IV', action_required=10, identifier='Notes Contributor', level=3, description='Contribute 10 Notes'),
			BadgeType(name='Notes Contributor V', action_required=20, identifier='Notes Contributor', level=3, description='Contribute 20 Notes'),

			# Tasks
			BadgeType(name='Classroom Task Contributor I', action_required=1, identifier='Classroom Task Contributor', description='Contribute on 1 Classroom Task'),
			BadgeType(name='Classroom Task Contributor II', action_required=2, identifier='Classroom Task Contributor', level=2, description='Contribute on 2 Classroom Tasks'),
			BadgeType(name='Classroom Task Contributor III', action_required=5, identifier='Classroom Task Contributor', level=3, description='Contribute on 5 Classroom Tasks'),
			BadgeType(name='Classroom Task Contributor IV', action_required=10, identifier='Classroom Task Contributor', level=4, description='Contribute on 10 Classroom Tasks'),
			BadgeType(name='Classroom Task Contributor V', action_required=20, identifier='Classroom Task Contributor', level=5, description='Contribute on 20 Classroom Tasks'),

			# Questions
			BadgeType(name='Questioner I', action_required=1, identifier='Questioner', description='Post 1 Question in Classroom'),
			BadgeType(name='Questioner II', action_required=2, identifier='Questioner', level=2, description='Post 2 Questions in Classroom'),
			BadgeType(name='Questioner III', action_required=5, identifier='Questioner', level=3, description='Post 5 Questions in Classroom'),
			BadgeType(name='Questioner IV', action_required=10, identifier='Questioner', level=4, description='Post 10 Questions in Classroom'),
			BadgeType(name='Questioner V', action_required=20, identifier='Questioner', level=5, description='Post 20 Questions in Classroom'),

			BadgeType(name='Answerer I', action_required=1, identifier='Answerer', description='Answer 1 Question in Classroom'),
			BadgeType(name='Answerer II', action_required=2, identifier='Answerer', level=2, description='Answer 2 Questions in Classroom'),
			BadgeType(name='Answerer III', action_required=5, identifier='Answerer', level=3, description='Answer 5 Questions in Classroom'),
			BadgeType(name='Answerer IV', action_required=10, identifier='Answerer', level=4, description='Answer 10 Questions in Classroom'),
			BadgeType(name='Answerer V', action_required=20, identifier='Answerer', level=5, description='Answer 20 Questions in Classroom'),

			BadgeType(name='Elite Answerer I', action_required=1, identifier='Elite Answerer', description='Solve 1 Question in Classroom'),
			BadgeType(name='Elite Answerer II', action_required=2, identifier='Elite Answerer', level=2, description='Solve 2 Questions in Classroom'),
			BadgeType(name='Elite Answerer III', action_required=5, identifier='Elite Answerer', level=3, description='Solve 5 Questions in Classroom'),
			BadgeType(name='Elite Answerer IV', action_required=10, identifier='Elite Answerer', level=4, description='Solve 10 Questions in Classroom'),
			BadgeType(name='Elite Answerer V', action_required=20, identifier='Elite Answerer', level=5, description='Solve 20 Questions in Classroom'),

			# Reports
			BadgeType(name='Community Contributor I', action_required=1, identifier='Community Contributor', description='Report 1 Wrongdoing or Post 1 Post in User Forum'),
			BadgeType(name='Community Contributor II', action_required=2, identifier='Community Contributor', level=2, description='Report 2 Wrongdoings or Post 2 Posts in User Forum'),
			BadgeType(name='Community Contributor III', action_required=5, identifier='Community Contributor', level=3, description='Report 3 Wrongdoings or Post 3 Posts in User Forum'),
			BadgeType(name='Community Contributor IV', action_required=10, identifier='Community Contributor', level=4, description='Report 4 Wrongdoings or Post 4 Posts in User Forum'),
			BadgeType(name='Community Contributor V', action_required=20, identifier='Community Contributor', level=5, description='Report 5 Wrongdoings or Post 5 Posts in User Forum'),
		])
	except IntegrityError:
		pass

	verify_email = Action.objects.get(name='verify_email')
	update_user_info = Action.objects.get(name='update_user_info')
	refer_friend = Action.objects.get(name='refer_friend')
	add_friend = Action.objects.get(name='add_friend')
	update_classroom_info = Action.objects.get(name='update_classroom_info')
	upload_file = Action.objects.get(name='upload_file')
	add_classroom_task = Action.objects.get(name='add_classroom_task')
	edit_classroom_task = Action.objects.get(name='edit_classroom_task')
	post_question = Action.objects.get(name='post_question')
	answer_question = Action.objects.get(name='answer_question')
	answer_approved = Action.objects.get(name='answer_approved')
	report_forum = Action.objects.get(name='report_forum')
	report_user = Action.objects.get(name='report_user')
	report_post = Action.objects.get(name='report_post')
	report_classroom_task = Action.objects.get(name='report_classroom_task')

	# Add Linked actions
	BadgeType.objects.get(name='Email Verified').linked_actions.add(verify_email)
	BadgeType.objects.get(name='Completed User Information').linked_actions.add(update_user_info)

	BadgeType.objects.get(name='Friend Referred I').linked_actions.add(refer_friend)
	BadgeType.objects.get(name='Friends Referred II').linked_actions.add(refer_friend)
	BadgeType.objects.get(name='Friends Referred III').linked_actions.add(refer_friend)

	BadgeType.objects.get(name='Classroom Contributor I').linked_actions.add(update_classroom_info)
	BadgeType.objects.get(name='Classroom Contributor II').linked_actions.add(update_classroom_info)
	BadgeType.objects.get(name='Classroom Contributor III').linked_actions.add(update_classroom_info)

	BadgeType.objects.get(name='Friend I').linked_actions.add(add_friend)
	BadgeType.objects.get(name='Friend II').linked_actions.add(add_friend)
	BadgeType.objects.get(name='Friend III').linked_actions.add(add_friend)
	BadgeType.objects.get(name='Friend IV').linked_actions.add(add_friend)
	BadgeType.objects.get(name='Friend V').linked_actions.add(add_friend)

	BadgeType.objects.get(name='Notes Contributor I').linked_actions.add(upload_file)
	BadgeType.objects.get(name='Notes Contributor II').linked_actions.add(upload_file)
	BadgeType.objects.get(name='Notes Contributor III').linked_actions.add(upload_file)
	BadgeType.objects.get(name='Notes Contributor IV').linked_actions.add(upload_file)
	BadgeType.objects.get(name='Notes Contributor V').linked_actions.add(upload_file)

	BadgeType.objects.get(name='Classroom Task Contributor I').linked_actions.add(add_classroom_task, edit_classroom_task)
	BadgeType.objects.get(name='Classroom Task Contributor II').linked_actions.add(add_classroom_task, edit_classroom_task)
	BadgeType.objects.get(name='Classroom Task Contributor III').linked_actions.add(add_classroom_task, edit_classroom_task)
	BadgeType.objects.get(name='Classroom Task Contributor IV').linked_actions.add(add_classroom_task, edit_classroom_task)
	BadgeType.objects.get(name='Classroom Task Contributor V').linked_actions.add(add_classroom_task, edit_classroom_task)

	BadgeType.objects.get(name='Questioner I').linked_actions.add(post_question)
	BadgeType.objects.get(name='Questioner II').linked_actions.add(post_question)
	BadgeType.objects.get(name='Questioner III').linked_actions.add(post_question)
	BadgeType.objects.get(name='Questioner IV').linked_actions.add(post_question)
	BadgeType.objects.get(name='Questioner V').linked_actions.add(post_question)

	BadgeType.objects.get(name='Answerer I').linked_actions.add(answer_question)
	BadgeType.objects.get(name='Answerer II').linked_actions.add(answer_question)
	BadgeType.objects.get(name='Answerer III').linked_actions.add(answer_question)
	BadgeType.objects.get(name='Answerer IV').linked_actions.add(answer_question)
	BadgeType.objects.get(name='Answerer V').linked_actions.add(answer_question)

	BadgeType.objects.get(name='Elite Answerer I').linked_actions.add(answer_approved)
	BadgeType.objects.get(name='Elite Answerer II').linked_actions.add(answer_approved)
	BadgeType.objects.get(name='Elite Answerer III').linked_actions.add(answer_approved)
	BadgeType.objects.get(name='Elite Answerer IV').linked_actions.add(answer_approved)
	BadgeType.objects.get(name='Elite Answerer V').linked_actions.add(answer_approved)

	BadgeType.objects.get(name='Community Contributor I').linked_actions.add(report_forum, report_user, report_post, report_classroom_task)
	BadgeType.objects.get(name='Community Contributor II').linked_actions.add(report_forum, report_user, report_post, report_classroom_task)
	BadgeType.objects.get(name='Community Contributor III').linked_actions.add(report_forum, report_user, report_post, report_classroom_task)
	BadgeType.objects.get(name='Community Contributor IV').linked_actions.add(report_forum, report_user, report_post, report_classroom_task)
	BadgeType.objects.get(name='Community Contributor V').linked_actions.add(report_forum, report_user, report_post, report_classroom_task)

	return Response({'detail': 'Done'}, status=status.HTTP_201_CREATED)
