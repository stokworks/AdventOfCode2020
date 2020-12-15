#! /usr/bin/env python

import sys

ITERS1 = 2020
TESTS1 = {
	'1,3,2': 1,
	'2,1,3': 10,
	'1,2,3': 27,
	'2,3,1': 78,
	'3,2,1': 438,
	'3,1,2': 1836
}
INPUT1 = '1,20,11,6,12,0'

ITERS2 = 30000000
TESTS2 = {
	'0,3,6': 175594,
	'1,3,2': 2578,
	'2,1,3': 3544142,
	'1,2,3': 261214,
	'2,3,1': 6895259,
	'3,2,1': 18,
	'3,1,2': 362
}
INPUT2 = INPUT1

TESTS = [(inp, exp, ITERS1) for inp, exp in TESTS1.items()] + \
		[(inp, exp, ITERS2) for inp, exp in TESTS2.items()]

PROGRESS_WIDTH = 50

def game_next(prevs, last_spoken):
	prev = prevs[-1]
	i0, i1 = last_spoken[prev] if prev in last_spoken else (-1, -1)
	n = i0 - i1 if i1 >= 0 else 0
	last_spoken[n] = (len(prevs), last_spoken[n][0] if n in last_spoken else -1)
	return n

def game(turns, iters):
	if iters > 10e6:
		sys.stdout.write('[' + (' ' * PROGRESS_WIDTH) + ']')
		sys.stdout.flush()
		sys.stdout.write('\b' * (PROGRESS_WIDTH + 1))

	turns = list(map(int, turns.split(',')))
	last_spoken = {t:(i, -1) for i, t in enumerate(turns)}
	while len(turns) < iters:
		turns.append(game_next(turns, last_spoken))

		if iters > 10e6 and len(turns) % (iters // PROGRESS_WIDTH) == 0:
			sys.stdout.write('#')
			sys.stdout.flush()

	if iters > 10e6:		
		sys.stdout.write(']\n')

	return turns[-1]

if __name__ == '__main__':
	for inp, exp, iters in TESTS:
		print('TEST input {}, {} iterations'.format(inp, iters))
		out = game(inp, iters)
		if out == exp:
			print('PASSED')
		else:
			print('FAILED: Expected {}, got {}.'.format(exp, out))

	print(game(INPUT1, ITERS1))
	print(game(INPUT2, ITERS2))