#! /usr/bin/env python

import sys

DIRS = {
	'se': (+1, -1,  0),
	'sw': (+1,  0, -1),
	'nw': (-1, +1,  0),
	'ne': (-1,  0, +1),
	'e' : ( 0, -1, +1),
	'w' : ( 0, +1, -1)
}

def do_step(pos, step):
	dz, dy, dx = DIRS[step]
	z, y, x = pos
	return (z + dz, y + dy, x + dx)

def do_walk(pos, route):
	if len(route) >= 2:
		if route[0:2] == 'se':
			return do_walk(do_step(pos, 'se'), route[2:])
		elif route[0:2] == 'sw':
			return do_walk(do_step(pos, 'sw'), route[2:])
		elif route[0:2] == 'nw':
			return do_walk(do_step(pos, 'nw'), route[2:])
		elif route[0:2] == 'ne':
			return do_walk(do_step(pos, 'ne'), route[2:])
	if len(route) >= 1:
		if route[0:1] == 'e':
			return do_walk(do_step(pos, 'e'), route[1:])
		elif route[0:1] == 'w':
			return do_walk(do_step(pos, 'w'), route[1:])
	return pos

if __name__ == '__main__':
	flips = []
	with open(sys.argv[1]) as f:
		for line in f:
			flips.append(line.strip())

	tiles = dict()

	for flip in flips:
		pos = do_walk((0,0,0), flip)
		if pos in tiles:
			tiles[pos] = not tiles[pos]
		else:
			tiles[pos] = True

	print(sum([int(t) for t in tiles.values()]))
