#! /usr/bin/env python

import sys

def apply_mask(mask, value):
	for i, b in enumerate(mask):
		if b == '1':
			value = value | (1 << (35 - i))
		elif b == '0':
			value = value & ~(1 << (35 - i))
	return value

if __name__ == '__main__':
	mem = dict()
	mask = 'X'*36

	with open(sys.argv[1]) as f:
		for l in f:
			l = l.strip()

			if l[:7] == 'mask = ':
				mask = l[7:]
			else:
				addr = l[l.index('[') + 1:l.index(']')]
				value = int(l[l.index('=') + 2:])
				mem[addr] = apply_mask(mask, value)

	print(sum(mem.values()))