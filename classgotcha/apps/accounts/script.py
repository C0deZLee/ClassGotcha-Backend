from django.utils import timezone
from datetime import datetime, timedelta
from django.db import models

from ..accounts.models import Account, Group
from ..classrooms.models import Classroom
from ..tasks.models import Task
# import Intervals 

# TODO download the intervals package
#def 

weekday_dict = {1:'Mo',2:'Tu',3:'We',4:'Th',5:'Fi'}
def get_user_free_intervals(account,date):
	# get week day from date
	weekday = weekday_dict[date.weekday]

	all_class = account.tasks.filter(category='Class',repeat__contains = weekday) # this is illigal need to find the right way to to it

	all_class_intervals = []

	for classe in all_class:
		all_class_intervals.append([classe.start,classe.end])

	all_customized_tasks = account.tasks.filter(category = 'Other',repeat = True ,repeat__contains = weekday)

	if all_customized_tasks:

		for customized_task in all_customized_tasks:

			all_class_intervals.append([customized_task.start,customized_task.end])

	all_non_repeat_tasks = account.tasks.filter(category = 'Other',repeat = False, start__date=date)

	if all_non_repeat_tasks:
		for customized_task in all_non_repeat_tasks:

			all_class_intervals.append([all_non_repeat_task.start,all_non_repeat_task.end])

	
	# find the union of all intervals

	intervals = Intervals.combine(all_class_intervals)
	

	# compute the complement of all the intervals


	free_intervals = Intervals.complement(free_intervals)




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
	if len(intervals) == 0:
		if first and last:
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
