#! /usr/bin/env python

import math
import sys

def slope(area, dx, dy):
	x = 0
	y = 0
	trees = 0

	for l in area:
		if y % dy == 0:
			trees += 1 if l[x % len(l)] == '#' else 0
			x += dx
		y += 1

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
