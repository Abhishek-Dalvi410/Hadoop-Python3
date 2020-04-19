#!/usr/bin/env python3

import sys
import re
import os
import fileinput



for line in fileinput.input():
	words= re.findall(r'\w+', line.strip())
	doc_id=os.environ["map_input_file"]
	doc_id=re.findall(r'\w+', doc_id)[-2]
	for word in words:
		print(word.lower(),"\t",doc_id)
