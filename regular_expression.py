# -*- coding: utf-8 -*-
import re

with open('input.txt', 'r') as f:
    data = f.read()


normal = "(\d+/\d+/\d+)"
normal_month_date = "(\d+/\d+)"
normal_year = '[0-9][0-9][0-9][0-9]'
holidays = "(New Year's Day|Inauguration Day|Martin Luther King, Jr. Day|George Washington’s Birthday|Memorial Day|Independence Day|Labor Day|Columbus Day|Veterans Day|Thanksgiving Day|Christmas Day)"
weeks = "(Sunday|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday)"
months = "(J[Aa][Nn][.a-z]*|F[Ee][Bb][.a-z]*|M[Aa][Rr][.a-z]*|A[Pp][Rr][.a-z]*|M[Aa][Yy][.a-z]*|J[Uu][Nn][.a-z]*|J[Uu][Ll][.a-z]*|A[Uu][Gg][.a-z]*|S[Ee][Pp][Tt][.a-z]*|O[Cc][Tt][.a-z]*|N[Oo][Vv][.a-z]*|D[Ee][Cc][.a-z]*)"
weeks_time = weeks + '( \d+(a.m.|p.m.|am|pm))'
weeks_periods = weeks + '( (morning|afternoon|evening))' 
months_date = months + ' [0-9]*[0-9]*(st|nd|rd|th)*,*\s*' + '([0-9][0-9][0-9][0-9])+'
months_date2 = months + ' [0-9]*[0-9]*(st|nd|rd|th)+'
weeks_date = weeks + ',*\s*' + months_date
months_date_with_para1 = 'the ' + '[0-9]*[0-9]*(st|nd|rd|th)* ' + 'of ' + months
months_date_with_para2 = 'the ' + '(first|second|third)' + ' of ' + months

result = []
for r in [normal, normal_month_date, normal_year, holidays, weeks, months, weeks_time, \
	      weeks_periods, months_date, months_date2, weeks_date, months_date_with_para1, 
	      months_date_with_para2]:
	match = re.finditer(r, data)
	for m in match:
		if m.group() not in result:
			result.append(m.group())
print(result)

with open("output.txt", "w") as output:
	for date in result:
		output.write(date + "\n")

