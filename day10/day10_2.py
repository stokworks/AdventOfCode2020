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
	
	n_ways = [0] * len(adapters)

	for i in range(len(n_ways)):
		if not adapters[i]:
			continue
		if i >= 3:
			n_ways[i] += n_ways[i - 1] + n_ways[i - 2] + n_ways[i - 3]
		elif i == 2:
			n_ways[i] += n_ways[i - 1] + n_ways[i - 2]
		elif i == 1:
			n_ways[i] += n_ways[i - 1]
		elif i == 0:
			n_ways[i] = 1

	print(n_ways[-1])