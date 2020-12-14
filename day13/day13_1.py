#! /usr/bin/env python

import sys

if __name__ == '__main__':
	leave = None
	schedule = []

	with open(sys.argv[1]) as f:
		for l in f:
			if not leave:
				leave = int(l)
			else:
				for t in l.strip().split(','):
					if t != 'x':
						schedule.append(int(t))

	early = min([((leave // t + 1) * t, t) for t in schedule])
	print((early[0] - leave) * early[1])