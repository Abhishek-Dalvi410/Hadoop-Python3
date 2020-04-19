#!/usr/bin/env python3
from itertools import groupby
from operator import itemgetter
import sys

def read_mapper_output(file, separator='\t'):
    for line in file:
        yield line.rstrip().split(separator, 1)

def main(separator='\t'):
    data = read_mapper_output(sys.stdin, separator=separator)
    for current_word, group in groupby(data, itemgetter(0)):
            try:
                    total_count = sum(int(count) for current_word, count in group)
                    print(current_word + separator + str(total_count))
            except ValueError:
                    pass

if __name__ == "__main__":
    main()