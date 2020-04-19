#!/usr/bin/python3
import sys
import pandas as pd
import numpy as np
from hdfs import InsecureClient
K = 5
header = sys.stdin.readline()
header = header.strip()
header = header.split(',')
train_data = []
client_hdfs = InsecureClient('http://localhost:9870')
with client_hdfs.read('/home/knn_input/Test.csv', encoding = 'utf-8') as reader:
	test_df = pd.read_csv(reader)
test_rows, test_cols = test_df.shape
for line in sys.stdin:
	line = line.strip()
	line = line.split(',')
	train_data.append(line)
train_df = pd.DataFrame(train_data, columns = header)
train_df = train_df.apply(pd.to_numeric)
test_df = test_df.apply(pd.to_numeric)
train_rows, train_cols = train_df.shape
labels = train_df.iloc[:, train_cols - 1]
train_df = train_df.iloc[:,:-1]
train_df.reset_index(drop=True)
test_df.reset_index(drop=True)
for i in range(test_rows):
	distances = ((train_df - test_df.iloc[i,:])**2).apply(lambda x: sum(x), axis = 1)
	min_indexes = distances.argsort()[:K]
	for j in min_indexes:
		print('%d\t%s'%(i + 1, str(distances[j]) + '$' + str(labels[j])))
			
