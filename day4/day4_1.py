#! /usr/bin/env python

import sys

if __name__ == '__main__':
	with open(sys.argv[1]) as f:
		ps_txt = f.read()

	ps = []

	for p_txt in ps_txt.split('\n\n'):
		p_txt = p_txt.replace('\n', ' ').strip()

		p = dict()
		for f_txt in p_txt.split(' '):
			k = f_txt.split(':')[0]
			v = f_txt.split(':')[1]

			p[k] = v

		ps.append(p)

	n_valid = 0
	for p in ps:
		is_valid = \
			'byr' in p and \
			'iyr' in p and \
			'eyr' in p and \
			'hgt' in p and \
			'hcl' in p and \
			'ecl' in p and \
			'pid' in p

		n_valid += 1 if is_valid else 0

	print(n_valid)