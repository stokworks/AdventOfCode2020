#! /usr/bin/env python

import sys

def apply_mask(mask, addr):
	for i, b in enumerate(mask):
		if b == '1' or b == 'X':
			addr = addr[:i] + b + addr[i+1:]
	return addr

def write_mem(mem, addr, value):
	xi = addr.find('X')

	if xi == -1:
		mem[addr] = value
	else:
		write_mem(mem, addr[:xi] + '0' + addr[(xi+1):], value)
		write_mem(mem, addr[:xi] + '1' + addr[(xi+1):], value)

if __name__ == '__main__':
	mem = dict()
	mask = 'X'*36

	with open(sys.argv[1]) as f:
		for l in f:
			l = l.strip()

			if l[:7] == 'mask = ':
				mask = l[7:]
			else:
				addr = "{0:b}".format(int(l[l.index('[') + 1:l.index(']')])).zfill(36)
				value = int(l[l.index('=') + 2:])

				addr = apply_mask(mask, addr)
				write_mem(mem, addr, value)

	print(sum(mem.values()))