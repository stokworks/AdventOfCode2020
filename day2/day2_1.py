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

			count = p.count(c)
			valid += int(count >= l and count <= h)

	print(valid)
