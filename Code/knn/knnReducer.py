#!/usr/bin/python3
import sys
import pandas as pd
K = 5
mapper_data = []
for line in sys.stdin:
	line = line.strip()
	test_row, distance_label = line.split('\t', 1)
	distance, label = distance_label.split('$')
	mapper_data.append([test_row, distance, label])
df = pd.DataFrame(mapper_data, columns = range(3))
df = df.apply(pd.to_numeric)
test_label_set = df[0].unique()
for i in test_label_set:
	df_1 = df[df[0] == i]
	df_1 = df_1.sort_values(by=[1])
	curr_label = (df_1[2])[: K].mode()[0]
	print (i, '\t', curr_label)
