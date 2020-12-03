#! /usr/bin/env python

import sys

if __name__ == '__main__':
	x = 0
	trees = 0

	with open(sys.argv[1]) as f:
		for l in f:
			l = l.strip()
			trees += 1 if l[x % len(l)] == '#' else 0
			x += 3

	print(trees)