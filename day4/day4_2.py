#! /usr/bin/env python

import re
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

	hgt_re = re.compile(r'^\d+(cm|in)$')
	hcl_re = re.compile(r'^#[0-9a-f]{6}$')
	ecl_re = re.compile(r'^(amb|blu|brn|gry|grn|hzl|oth)$')
	pid_re = re.compile(r'^[0-9]{9}$')

	n_valid = 0

	for p in ps:
		is_valid = \
			'byr' in p and \
			int(p['byr']) >= 1920 and \
			int(p['byr']) <= 2002 and \
			'iyr' in p and \
			int(p['iyr']) >= 2010 and \
			int(p['iyr']) <= 2020 and \
			'eyr' in p and \
			int(p['eyr']) >= 2020 and \
			int(p['eyr']) <= 2030 and \
			'hgt' in p and \
			hgt_re.match(p['hgt']) and \
			((p['hgt'][-2:] == 'cm' and int(p['hgt'][:-2]) >= 150 and int(p['hgt'][:-2]) <= 193) or \
			(p['hgt'][-2:] == 'in' and int(p['hgt'][:-2]) >= 59 and int(p['hgt'][:-2]) <= 76)) and \
			'hcl' in p and \
			hcl_re.match(p['hcl']) and \
			'ecl' in p and \
			ecl_re.match(p['ecl']) and \
			'pid' in p and \
			pid_re.match(p['pid'])

		n_valid += 1 if is_valid else 0

	print(n_valid)