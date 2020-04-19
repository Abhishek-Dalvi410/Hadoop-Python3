#!/usr/bin/python3
import sys
import itertools
import operator
dict = {}
for line in sys.stdin:
    line = line.strip()
    #lines = line.split('\t')
    _,lines = line.split('\t', 1)
    trigram,count = lines.split('\t',1)
    #trigram = lines[0]
#line.split('\t')
    #count = lines[1]
    #print(type(count))
    if trigram not in dict:
        dict[trigram] = int(count)
    else:
        dict[trigram]=dict[trigram]+ int(count)
#dict = {k: v for k, v in sorted(dict.items(), key = lambda item: item[1], reverse = True)}
dict1 = sorted(dict.items(), key = operator.itemgetter(1), reverse = True)
#print(dict1)
top_ten = list(itertools.islice(dict1, 10))
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
