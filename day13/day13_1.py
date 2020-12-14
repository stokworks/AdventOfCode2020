#! /usr/bin/env python

import sys

if __name__ == '__main__':
	leave = None
	schedule = []

	with open(sys.argv[1]) as f:
		l = f.read().split('\n')
		leave = int(l[0])

		for t in l[1].split(','):
			if not t == 'x':
				schedule.append(int(t))

	early = min([((leave // t + 1) * t, t) for t in schedule])
	print((early[0] - leave) * early[1])