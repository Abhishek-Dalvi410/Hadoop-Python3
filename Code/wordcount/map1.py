#!/usr/bin/env python3
import string
import sys
import re 
def read_input(file):
    for line in file:
        line = line.lower()
        line = re.sub('[^a-zA-Z0-9  \n]','',line)           
        yield line.split()

def main(separator='\t'):
    data = read_input(sys.stdin)
    for words in data:
            for word in words:
                    print(word, separator, 1)

if __name__ == "__main__":
    main()
