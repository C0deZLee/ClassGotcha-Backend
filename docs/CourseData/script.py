import json

f = open('docs/CourseData/courses_data_format.json')
f2 = open('docs/CourseData/email.json')

format = json.load(f)
email = json.load(f2)

# for key, value in format.iteritems():
# 	if 'instructor1' in value and value['instructor1'] == 'Staff':
# 		value.pop('instructor1', None)
# 	if 'instructor2' in value:
# 		value.pop('instructor2', None)
#
for key, value in format.iteritems():
	if 'instructor1' in value:
		for key2, value2 in email.iteritems():
			if value['instructor1'] == key2 and '@psu.edu' in value2:
				value['instructor1_email'] = value2
				continue
	if 'instructor2' in value:
		for key2, value2 in email.iteritems():
			if value['instructor2'] == key2 and '@psu.edu' in value2:
				value['instructor2_email'] = value2
				continue

with open('docs/CourseData/format2.json', 'w') as ffff:
	json.dump(format, ffff)
	print 'done'
