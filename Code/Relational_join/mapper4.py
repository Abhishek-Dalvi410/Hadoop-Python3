#!/usr/bin/env python3

import sys


for line in sys.stdin:
	emp_id="-1"
	name="-1"
	salary="-1"
	country="-1"
	passcode="-1"
	line=line.strip()
	splits=line.split("\t")
	#print(splits)
	if(len(splits)==2):
		emp_id=splits[0]
		name=splits[1]
	elif(len(splits)>2):
		emp_id=splits[0]
		salary=splits[1]
		country=splits[2]
		passcode=splits[3]
	else:
		continue
	print(emp_id+"\t"+name+"\t"+salary+"\t"+country+"\t"+passcode)
	
