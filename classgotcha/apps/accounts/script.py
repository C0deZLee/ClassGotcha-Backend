from django.utils import timezone
from django.db import models
from datetime import datetime, timedelta, time, date

from ..accounts.models import Account, Group
from ..classrooms.models import Classroom
from ..tasks.models import Task

def test_scheduler():
	account = Account.objects.all().filter(username='test1')[0]
	task = account.tasks.all().filter(category=1)[0]
	generate_recommendations_for_homework(account, task)


def generate_recommendations(account, task, pre_days=2):
	due_day = task.end
	work_day = (due_day - timedelta(days=pre_days)).day()
	title = {
		1: "Do ",
		2: "Prepare for ",
		3: "Prepare for "
	}[task.category] + task.task_name + ' of %s' % task.task_of_classroom.class_short if task.task_of_classroom else ''

	# get the user's free time (within 8-24)
	free_intervals = get_user_free_intervals(account=account, day=work_day, start=time(9,0), end=time(23,59,59))
	
	#print free_intervals
	for interval in free_intervals:
		# find appropriate time to do things
		if interval[1] - interval[0] > timedelta(hours=1, minutes=30):
			new_task = Task.objects.create(
				task_name=title,
				category=6,
				start=datetime.combine(work_day, interval[0]+timedelta(minutes=15)),
				end=datetime.combine(work_day, interval[0]+timedelta(minutes=75)),
				classroom=task.task_of_classroom, creator=account)
			new_task.involved.add(account)
			return False
	return True
	


def generate_recommendations_for_user(account, task):  # in this case the end time of the task is the due day
	for d in [2,5,10][0:task.category]:
		while generate_recommendations(account, task, pre_days=d):
			d += 1
	return



def get_user_free_intervals(account, day, start = time(0,0,0), end = time(23,59,59)):
	busy_intervals = []
	weekday = day.strftime("%a")[0:2] # Get the first two characters of weekday string

	tasks = account.tasks.filter(category__in=[0,3,5,6], repeat__contains=weekday, )
	busy_intervals += [(task.start.time, task.end.time) for task in tasks]
	
	# all_non_repeat_tasks = account.tasks.filter(category=6, start__year=day.year, start__month=day.month, start__day=day.day)
	all_non_repeat_tasks = account.tasks.filter(category=6, start=day)
	busy_intervals += [(task.start.time, task.end.time) for task in all_non_repeat_tasks]

	intervals = combine(busy_intervals) # union

	# compute the complement of all the intervals
	free_intervals = complement(intervals, first=start, last=end)

	return free_intervals


# Copied from http://nullege.com/codes/search/Intervals.complement
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
	if first < last_from:
		new_intervals.append((first, last_from))
	for this_from, this_to in intervals[1:]:
		if this_from > last_to:
			new_intervals.append((last_to, this_from))
		last_from = this_from
		last_to = max(last_to, this_to)
	if last and last > last_to:
		new_intervals.append((last_to, last))
	return new_intervals


def combine(intervals):
	"""
	combine intervals.

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
