#! /usr/bin/env python

import sys

def turn(d, times):
	dx, dy = d
	times = times % 4
	if times == 0:
		return d
	elif times == 1:
		return (-dy, dx)
	elif times == 2:
		return (-dx, -dy)
	elif times == 3:
		return (dy, -dx)

if __name__ == '__main__':
	d = (1, 0)
	x = 0
	y = 0

	with open(sys.argv[1]) as f:
		for r in f:
			ins = r[0]
			num = int(r[1:])
			if ins == 'N':
				y -= num
			elif ins == 'S':
				y += num
			elif ins == 'E':
				x += num
			elif ins == 'W':
				x -= num
			elif ins == 'L':
				d = turn(d, -num/90)
			elif ins == 'R':
				d = turn(d, num/90)
			elif ins == 'F':
				x += d[0] * num
				y += d[1] * num

	print(abs(x) + abs(y))