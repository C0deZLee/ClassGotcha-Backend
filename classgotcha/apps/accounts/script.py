from django.utils import timezone
from datetime import datetime, timedelta
from django.db import models

from ..accounts.models import Account, Group
from ..classrooms.models import Classroom
from ..tasks.models import Task
from datetime import datetime, timedelta


# import Intervals

# TODO download the intervals package


def test_scheduler():
	account = Account.objects.all().filter(username='test1')[0]
	# print account.tasks.all().filter(category = 1)[0]
	task = account.tasks.all().filter(category=1)[0]
	generate_recommendations_for_homework(account, task)


def generate_recommendations_for_exam(account,task):

	due_date = task.end
	work_date = due_date - timedelta(days=7)  # in this default setting do the homework 2 days prior to the due date
	# get the user's free time
	free_intervals = get_user_free_intervals(account=account, date=work_date)
	# print free_intervals
	task_add = False
	for interval in free_intervals:
		# find appropriate time to do things
		if (interval[0] > 8) and (interval[1] < 20) and (interval[1] - interval[0] > 1):
			# generate a new task to do the homework
			try:
				new_task = Task(task_name='do homework for' + task.task_name,
				                category=6,
				                start=datetime(work_date.year, work_date.month, work_date.day, int(interval[0]), int(60 * (interval[0] - int(interval[0])))),
				                end=datetime(work_date.year, work_date.month, work_date.day, int(interval[1]), int(60 * (interval[1] - int(interval[1])))),
				                classroom=task.classroom, creator=account)

				new_task.save()
				task_add = True
				break
			except:
				pass

		for start in range(9, 18):
			if (interval[1] - 1) > start > interval[0]:
				try:
					new_task = Task(task_name='do homework for' + task.task_name,
					                category=6,
					                start=datetime(work_date.year, work_date.month, work_date.day, start, 0),
					                end=datetime(work_date.year, work_date.month, work_date.day, start + 1, 0),
					                classroom=task.classroom, creator=account)
					new_task.save()
					task_add = True
					break
				except:
					pass
		if task_add:
			break
	return task_add


def generate_recommendations(account,task,description = 'do homework for ',pre_days=2):
	
	due_date = task.end
	work_date = due_date - timedelta(days=pre_days)  # in this default setting do the homework 2 days prior to the due date
	

	# get the user's free time
	free_intervals = get_user_free_intervals(account=account, date=work_date)
	
	#print free_intervals
	task_add = False
	for interval in free_intervals:
		# find appropriate time to do things
		if (interval[0] > 8) and (interval[1] < 24) and (interval[1] - interval[0] > 1):
			# generate a new task to do the homework
			try:
				new_task = Task(task_name=description + task.task_name,
				                category=6,
				                start=datetime(work_date.year, work_date.month, work_date.day, int(interval[0]), int(60 * (interval[0] - int(interval[0])))),
				                end=datetime(work_date.year, work_date.month, work_date.day, int(interval[1]), int(60 * (interval[1] - int(interval[1])))),
				                classroom=task.task_of_classroom, creator=account)

				new_task.save()
				task_add = True
				break
			except:
				pass

		for start in range(9, 24):
			if (interval[1] - 1) > start > interval[0]:
				new_task = Task(task_name=description + task.task_name,
					                category=6,
					                start=datetime(work_date.year, work_date.month, work_date.day, start, 0),
					                end=datetime(work_date.year, work_date.month, work_date.day, start + 1, 0),
					                classroom=task.task_of_classroom, creator=account)

				new_task.save()
				new_task.involved.add(account)
				account.tasks.add(new_task)
				account.save()
				new_task.save()
				try:
					
					new_task = Task(task_name=description + task.task_name,
					                category=6,
					                start=datetime(work_date.year, work_date.month, work_date.day, start, 0),
					                end=datetime(work_date.year, work_date.month, work_date.day, start + 1, 0),
					                classroom=task.task_of_classroom, creator=account)
					new_task.save()
					task_add = True
					break
				except:
					pass
		if task_add:
			break
	return task_add
	


def generate_recommendations_for_user(account, task):  # in this case the end time of the task is the due date
	
	if task.category==1:
		generate_recommendations(account,task,pre_days=2)

	elif task.category==2:
		generate_recommendations(account,task,description = 'Prepare for the Quiz',pre_days=2)
		generate_recommendations(account,task,description = 'Prepare for the Quiz',pre_days=7)

	elif task.category==3:
		generate_recommendations(account,task,description = 'Prepare for the Exam',pre_days=2)
		generate_recommendations(account,task,description ='Prepare for the Exam',pre_days=7)
		generate_recommendations(account,task,description ='Prepare for the Exam',pre_days=14)

	else:

		pass

	return 1



weekday_dict = {1: 'Mo', 2: 'Tu', 3: 'We', 4: 'Th', 5: 'Fi' ,6:'Sat',0:'Sun'}


def get_user_free_intervals(account, date):
	# get week day from date

	# print date
	weekday = weekday_dict[date.weekday()]
	# print weekday
	all_class = account.tasks.filter(category=0, repeat__contains=weekday)  # this is illigal need to find the right way to to it
	# print all_class
	all_class_intervals = []

	for classe in all_class:
		all_class_intervals.append([float(classe.start.hour + float(classe.start.minute) / 60), float(classe.end.hour + float(classe.end.minute) / 60)])
		#print [float(classe.start.hour + float(classe.start.minute) / 60), float(classe.end.hour + float(classe.end.minute) / 60)]
	all_customized_tasks = account.tasks.filter(category=6, repeat=True, repeat__contains=weekday)
	if all_customized_tasks:
		for customized_task in all_customized_tasks:
			all_class_intervals.append([float(customized_task.start.hour + float(customized_task.start.minute) / 60), float(customized_task.end.hour + float(customized_task.end.minute) / 60)])
			#print [float(customized_task.start.hour + float(customized_task.start.minute) / 60), float(customized_task.end.hour + float(customized_task.end.minute) / 60)]
	all_non_repeat_tasks = account.tasks.filter(category=6, start__year=date.year,start__month=date.month, start__day=date.day)
	#print date.month,date.day,date.year
	#print all_non_repeat_tasks

	if all_non_repeat_tasks:
		for customized_task in all_non_repeat_tasks:
			#print 'here'
			all_class_intervals.append([float(customized_task.start.hour + float(customized_task.start.minute) / 60), float(customized_task.end.hour + float(customized_task.end.minute) / 60)])
			#print [float(customized_task.start.hour + float(customized_task.start.minute) / 60), float(customized_task.end.hour + float(customized_task.end.minute) / 60)]
	# find the union of all intervals

	print all_class_intervals
	intervals = combine(all_class_intervals)

	# print intervals
	# print all_class_intervals
	# compute the complement of all the intervals
	free_intervals = complement(intervals, first=1, last=24)
	# print free_intervals

	return free_intervals


def group(data):
	data = sorted(data)
	it = iter(data)
	a, b = next(it)
	for c, d in it:
		if b >= c:  # Use `if b > c` if you want (1,2), (2,3) not to be
			b = max(b, d)
		else:
			yield a, b
			a, b = c, d
	yield a, b


# http://nullege.com/codes/search/Intervals.complement
def complement(intervals, first=None, last=None):
	"""
	complement a list of intervals with intervals not in list.
	"""
	# print 'intervals', intervals
	if len(intervals) == 0:
		if (first or first == 0) and last:
			# print "here"
			return [(first, last)]
		else:
			return []
	new_intervals = []
	intervals.sort()
	last_from, last_to = intervals[0]
	if first and first < last_from:
		new_intervals.append((first, last_from))
	for this_from, this_to in intervals:
		if this_from > last_to:
			new_intervals.append((last_to, this_from))
		last_from = this_from
		last_to = max(last_to, this_to)
	if last and last > last_to:
		new_intervals.append((last_to, last))
	return new_intervals


def combine(intervals):
	"""combine intervals.

	Overlapping intervals are concatenated into larger intervals.
	"""
	if not intervals:
		return []

	new_intervals = []

	intervals.sort()
	first_from, last_to = intervals[0]

	for this_from, this_to in intervals[1:]:
		if this_from > last_to:
			new_intervals.append((first_from, last_to))
			first_from, last_to = this_from, this_to
			continue

		if last_to < this_to:
			last_to = this_to

	new_intervals.append((first_from, last_to))

	return new_intervals
