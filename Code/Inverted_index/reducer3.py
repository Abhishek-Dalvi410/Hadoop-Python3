#!/usr/bin/env python3


import sys
import re

index = dict()
docs=[]
for line in sys.stdin:
	word, doc_id = line.split('\t')
	doc_id=doc_id.rstrip()
	if(word in index):
		if(doc_id in index[word]):
			continue
		else:
			s=index[word]
			index[word]=s+str(doc_id)+" "
	else:
		index[word]=str(doc_id)+" "
for key,value in index.items():
	print(key,":",value)
