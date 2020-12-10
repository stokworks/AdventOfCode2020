#! /usr/bin/env python

import sys

TARGET = 2020

if __name__ == '__main__':
	with open(sys.argv[1]) as f:
		inputs = [int(n) for n in f]

	for i, n1 in enumerate(inputs):
		for j, n2 in enumerate(inputs[i+1:]):
			for n3 in inputs[i+j+1:]:
				if n1 + n2 + n3 == TARGET:
					print(n1 * n2 * n3)
