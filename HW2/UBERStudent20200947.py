#!/usr/bin/python3

import sys
from datetime import datetime, date
days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

def what_day_is_it(date):
    day = date.weekday()
    return(days[day])

input_file = sys.argv[1]
output_file = sys.argv[2]
region_list = []

with open(input_file) as file:
    for line in file:
        cnt = 1
        for r in line.split(","):
            if cnt % 4 == 1:
                region_list.append(r)
            cnt += 1

region_list = list(set(region_list))
region_dict = {}
day_dict = {"MON": [0, 0], "TUE": [0, 0], "WED": [0, 0], "THU": [0, 0], "FRI": [0, 0], "SAT": [0, 0], "SUN": [0, 0]}
for r in region_list:
    region_dict[r] = day_dict

for r in region_dict:
    list = [0, 0]
    with open(input_file) as file:
        for line in file:
            if r in line:
                l = line.split(",")
                
                date_format = "%m/%d/%Y"
                date = datetime.strptime(l[1], date_format)
                        
                day = what_day_is_it(date)
                
                region_dict[r][day][0] += int(l[2])
                region_dict[r][day][1] += int(l[3])

with open(output_file, "w", encoding="utf-8") as file:
    for r in region_dict:
        for d in days:
            file.write("{},{} {},{}\n".format(r, d, region_dict[r][d][0], region_dict[r][d][1]))