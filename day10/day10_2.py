#! /usr/bin/env python

import time
import sys

if __name__ == '__main__':
	a = [0, 0, 1]
	with open(sys.argv[1]) as f:
		for num in f:
			x = int(num.strip()) + 2
			if x >= len(a):
				a.extend([0] * (x - len(a) + 1))
			a[x] = 1

	a.extend([0, 0, 1])

	n = [0] * len(a)
	n[2] = 1
	for i in range(3, len(n)):
		n[i] = sum(n[i-3:i]) * a[i]
	print(n[-1])
