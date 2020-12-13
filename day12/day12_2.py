#! /usr/bin/env python

import sys

def turn(wx, wy, times):
	times = times % 4
	if times == 0:
		return (wx, wy)
	elif times == 1:
		return (-wy, wx)
	elif times == 2:
		return (-wx, -wy)
	elif times == 3:
		return (wy, -wx)

if __name__ == '__main__':
	x = 0
	y = 0
	wx = 10
	wy = -1

	with open(sys.argv[1]) as f:
		for r in f:
			ins = r[0]
			num = int(r[1:])
			if ins == 'N':
				wy -= num
			elif ins == 'S':
				wy += num
			elif ins == 'E':
				wx += num
			elif ins == 'W':
				wx -= num
			elif ins == 'L':
				wx, wy = turn(wx, wy, -num/90)
			elif ins == 'R':
				wx, wy = turn(wx, wy, num/90)
			elif ins == 'F':
				x += wx * num
				y += wy * num

	print(abs(x) + abs(y))