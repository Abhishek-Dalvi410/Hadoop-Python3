#!/usr/bin/python3
import sys
from itertools import islice
import operator
dict = {}
for line in sys.stdin:
	line = line.strip()
	trigram, count = line.split('\t', 1)
	if trigram not in dict:
		dict[trigram] = 1
	else:
		dict[trigram] += 1
#dict = {k: v for k, v in sorted(dict.items(), key = lambda item: item[1], reverse = True)}
dict = sorted(dict.items(), key = operator.itemgetter(1), reverse = True)
top_ten = list(islice(dict, 10))
for i in top_ten:
	print(i[0],"\t",i[1])
try:
	sys.stdout.close()
except:
	pass
try:
	sys.stderr.close()
except:
	pass
