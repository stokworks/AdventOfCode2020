#! /usr/bin/env python

from sympy import Matrix
from diophantine import solve
import itertools
import sys

if __name__ == '__main__':
	leave = None
	schedule = []

	with open(sys.argv[1]) as f:
		for l in f:
			if not leave:
				leave = int(l)
			else:
				i = 0
				for t in l.strip().split(','):
					if not t == 'x':
						schedule.append((int(t), i))
					i += 1

	combinations = list(itertools.combinations(schedule, 2))
	A = []
	b = []

	for x, y in combinations:
		row = [0] * len(schedule)
		vx, ix = x
		vy, iy = y
		row[schedule.index(x)] = vx
		row[schedule.index(y)] = -vy
		A.append(row)
		b.append(ix - iy)

	A = Matrix(A)
	b = Matrix(b)
	x = solve(A, b)

	print(x[0][0] * schedule[0][0])
