#!/usr/bin/env python3

import sys

users={}
users2={}

for line in sys.stdin:
	info=[]
	line= line.strip()
	splits=line.split("\t")
	eid=splits[0]
	name=splits[1]
	salary=splits[2]
	country=splits[3]
	passcode=splits[4]
	#info.append(eid)
	info.append(name)
	info.append(salary)
	info.append(country)
	info.append(passcode)
	if(eid in users):
		if(name=="-1"):
			info[0]=users[eid][0]
			users[eid]=info
		elif(country=="-1"):
			info=users[eid]
			info[0]=name
			users[eid]=info
	else:
		users[eid]=info
for key,value in users.items():
	n_values=""
	for in_values in value:
		n_values=n_values+in_values+"\t"
	print(key,"\t",n_values.strip())
	
