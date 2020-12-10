#! /usr/bin/env python

import sys

N_QUESTIONS = 26

if __name__ == '__main__':
	with open(sys.argv[1]) as f:
		fs_txt = f.read()

	fs = []

	for f_txt in fs_txt.split('\n\n'):
		qss = f_txt.replace('\n', ' ').strip().split(' ')

		qs_0 = qss[0]
		qss = qss[1:]

		f = [False] * N_QUESTIONS

		for q in qs_0:
			f[ord(q) - ord('a')] = True

		for qs in qss:
			for q in range(len(f)):
				if f[q] and not chr(q + ord('a')) in qs:
					f[q] = False

		fs.append(f)

	print(sum(list(f.count(True) for f in fs)))