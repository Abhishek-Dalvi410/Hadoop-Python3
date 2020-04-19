#!/usr/bin/python3
import sys
import re
import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
words = []
trigrams = []
list_of_keywords = ['science', 'fire', 'sea']
for line in sys.stdin:
	line = line.strip()
	words.extend(line.split())
words = list(map(lambda x: lemmatizer.lemmatize(re.sub('[^A-Za-z\-]+', '', x)), words))
words = list(map(lambda x: x.lower(), words))
words = list(map(lambda x: re.sub('science|fire|sea', '$', x), words))
for i in range(len(words)):
	if '$' in words[i]:
		try:
			if '$' not in words[i-2] and '$' not in words[i-1]:
				trigrams.append(words[i-2] + '_' + words[i-1] + '_' + words[i])
		except:
			pass
		try:
			if '$' not in words[i-1]:
				trigrams.append(words[i-1] + '_' + words[i] + '_' + words[i+1])
		except:
			pass
		try:
			if i < len(words) - 2:
				trigrams.append(words[i] + '_' + words[i+1] + '_' + words[i+2])
		except:
			pass
for trigram in trigrams:
	print(trigram,"\t", 1)
