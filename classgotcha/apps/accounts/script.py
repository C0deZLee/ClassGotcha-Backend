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
