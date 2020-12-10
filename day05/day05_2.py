#! /usr/bin/env python

import sys

def pass2id(pass_txt):
	row_txt = pass_txt[:-3].replace('F', '0').replace('B', '1')
	col_txt = pass_txt[-3:].replace('L', '0').replace('R', '1')
	return int(row_txt, 2) * 8 + int(col_txt, 2)

if __name__ == '__main__':
	seats = [False] * pass2id('BBBBBBBRRR')

	with open(sys.argv[1]) as f:
		for x in f:
			seats[pass2id(x.strip())] = True

	for i in range(len(seats)):
		if seats[i-1] and not seats[i] and seats[i+1]:
			print(i)