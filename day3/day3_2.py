#! /usr/bin/env python

import math
import sys

TREE = '#'

def slope(area, dx, dy):
	x = 0
	trees = 0

	for y, l in enumerate(area):
		if y % dy == 0:
			trees += 1 if l[x % len(l)] == TREE else 0
			x += dx

	return trees

if __name__ == '__main__':
	area = []

	with open(sys.argv[1]) as f:
		for l in f:
			area.append(l.strip())

	print(math.prod([
		slope(area, 1, 1),
		slope(area, 3, 1),
		slope(area, 5, 1),
		slope(area, 7, 1),
		slope(area, 1, 2)
	]))
