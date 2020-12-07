#! /usr/bin/env python

import sys

N_QUESTIONS = 26

if __name__ == '__main__':
	with open(sys.argv[1]) as f:
		fs_txt = f.read()

	gs = []

	for f_txt in fs_txt.split('\n\n'):
		f_txt = f_txt.replace('\n', '').strip()

		g = [False] * N_QUESTIONS
		for qs in f_txt.split(' '):
			for q in qs:
				g[ord(q) - ord('a')] = True

		gs.append(a)

	print(sum(list(f.count(True) for f in fs)))