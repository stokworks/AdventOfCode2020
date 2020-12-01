#! /usr/bin/env python

import sys

TARGET = 2020

if __name__ == '__main__':
	with open(sys.argv[1]) as f:
		inputs = [int(n) for n in f]

	for i, n1 in enumerate(inputs):
		for n2 in inputs[i+1:]:
			if n1 + n2 == TARGET:
				print('n1 = {}'.format(n1))
				print('n2 = {}'.format(n2))
				print('product = {}'.format(n1 * n2))
				sys.exit()

	print('Could not find solution.')