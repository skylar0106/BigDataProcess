#!/usr/bin/python3

import csv
import math 
from openpyxl import * 

wb = load_workbook(filename = 'student.xlsx')
ws = wb.active

total_list = []

i = 2
for row in ws.iter_rows(min_row = 2, max_row = ws.max_row):
	total = float(row[2].value) * 0.3 + float(row[3].value) * 0.35 + float(row[4].value) * 0.34 + float(row[5].value) * 0.01
	ws.cell(row = row[0].row, column = 7, value = round(total, 2))
	total_list.append(round(total, 2))	

A_students = math.trunc((ws.max_row - 2 + 1) * 0.3)
B_students = math.trunc((ws.max_row - 2 + 1) * 0.7)
A_list = []
B_list = []
C_list = []

cnt = 0 
while cnt < A_students:
	A_max = 0 
	for index, t in enumerate(total_list):
		if t not in A_list:
			if A_max < t:
				A_max = t
	if(A_max < 40):
		break
	A_list.append(A_max)	
	cnt += 1

cnt = 0
while cnt < B_students - A_students:
	B_max = 0
	for index, t in enumerate(total_list):
		if t not in A_list:
			if t not in B_list:
				if B_max < t:
					B_max = t
	if(B_max < 40):
		break
	B_list.append(B_max)	
	cnt += 1

while 1==1:
	C_max = 0
	for index, t in enumerate(total_list):
		if t not in A_list:
			if t not in B_list:
				if t not in C_list:
					if C_max < t:
						C_max = t
	if(C_max < 40):
		break
	C_list.append(C_max)

for index, a in enumerate(A_list):
	if index < math.trunc(len(A_list)/2):
		ws.cell(row = total_list.index(a) + 2, column = 8, value = 'A+')
	else:
		ws.cell(row = total_list.index(a) + 2, column = 8, value = 'A')

for index, b in enumerate(B_list):
	if index < math.trunc(len(B_list)/2):
		ws.cell(row = total_list.index(b) + 2, column = 8, value = 'B+')
	else:
		ws.cell(row = total_list.index(b) + 2, column = 8, value = 'B')

for index, c in enumerate(C_list):
	if index < math.trunc(len(C_list)/2):
		ws.cell(row = total_list.index(c) + 2, column = 8, value = 'C+')
	else:
		ws.cell(row = total_list.index(c) + 2, column = 8, value = 'C')

for t in total_list:
	if t < 40:
		ws.cell(row = total_list.index(t) + 2, column = 8, value = 'F')

wb.save('student.xlsx')
