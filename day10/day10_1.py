#! /usr/bin/env python

import sys

if __name__ == '__main__':
	adapters = [True]
	with open(sys.argv[1]) as f:
		for num in f:
			a = int(num.strip())
			if a >= len(adapters):
				adapters.extend([False] * (a - len(adapters) + 1))
			adapters[a] = True

	adapters.extend([False, False, True])

	one_step = 0
	three_step = 0
	index = 0

	while index < len(adapters) - 1:
		one_step += int(adapters[index + 1])
		three_step += int(not adapters[index + 1])
		index += 1 if adapters[index + 1] else 3

	print(one_step * three_step)