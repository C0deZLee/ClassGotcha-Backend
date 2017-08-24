from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from models import Action


@api_view(['GET'])
@permission_classes((IsAdminUser,))
def action_init(request):
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
		Action(name='report_classroom_task', exp=5),

		# Questions
		Action(name='post_question', exp=5),
		Action(name='answer_question', exp=5),
		Action(name='answer_approved', exp=15),

		# Reports
		Action(name='post', exp=1),
		Action(name='report_bug', exp=5),
		Action(name='report_issue', exp=5)
	])
	return Response({'detail': 'Done'}, status=status.HTTP_201_CREATED)
