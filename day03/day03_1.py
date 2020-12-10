#! /usr/bin/env python

import sys

DX = 3
TREE = '#'

if __name__ == '__main__':
	x = 0
	trees = 0

	with open(sys.argv[1]) as f:
		for l in f:
			l = l.strip()
			trees += 1 if l[x % len(l)] == TREE else 0
			x += DX

	print(trees)