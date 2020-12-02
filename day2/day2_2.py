#! /usr/bin/env python

import sys

if __name__ == '__main__':
	valid = 0

	with open(sys.argv[1]) as f:
		for x in f:
			p = x.split(':')[1][1:] # password
			c = x.split(':')[0][-1] # character
			l = int(x.split('-')[0]) # lower bound
			h = int(x.split('-')[1].split(' ')[0]) # upper bound

			valid += int((p[l-1] == c) != (p[h-1] == c))

	print(valid)
