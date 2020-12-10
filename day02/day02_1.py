#! /usr/bin/env python

import re
import sys

if __name__ == '__main__':
	valid = 0

	pattern = re.compile(r'(\d+)-(\d+) (\w): (\w+)')

	with open(sys.argv[1]) as f:
		for x in f:
			l, h, c, p = pattern.search(x).groups()
			count = p.count(c)
			valid += int(count >= int(l) and count <= int(h))

	print(valid)
