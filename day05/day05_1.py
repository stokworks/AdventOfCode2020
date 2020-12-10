#! /usr/bin/env python

import sys

def pass2id(pass_txt):
	row_txt = pass_txt[:-3].replace('F', '0').replace('B', '1')
	col_txt = pass_txt[-3:].replace('L', '0').replace('R', '1')
	return int(row_txt, 2) * 8 + int(col_txt, 2)

if __name__ == '__main__':
	with open(sys.argv[1]) as f:
		print(max([pass2id(x.strip()) for x in f]))
