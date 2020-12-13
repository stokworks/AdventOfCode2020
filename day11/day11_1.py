#! /usr/bin/env python

import copy
import sys

NONE = '.'
EMPTY = 'L'
OCCUPIED = '#'

def count_adjecent(seats, y, x):
	n_occupied = 0
	for dy in range(-1, 2):
		for dx in range(-1, 2):
			if dy == 0 and dx == 0:
				continue
			n_occupied += int(seats[y + dy][x + dx] == OCCUPIED)
	return n_occupied

def do_round(seats):
	new_seats = copy.deepcopy(seats)
	changed = False

	for y in range(1, len(seats)-1):
		for x in range(1, len(seats[0])-1):
			if seats[y][x] == EMPTY and count_adjecent(seats, y, x) == 0:
				new_seats[y][x] = OCCUPIED
				changed = True
			elif seats[y][x] == OCCUPIED and count_adjecent(seats, y, x) >= 4:
				new_seats[y][x] = EMPTY
				changed = True

	return new_seats, changed

if __name__ == '__main__':
	seats = []
	with open(sys.argv[1]) as f:
		for l in f:
			seats.append(list(l.strip()))

	seats.insert(0, ['.'] * len(seats[0]))
	seats.append(['.'] * len(seats[0]))
	seats = [['.'] + row + ['.'] for row in seats]

	keep_going = True
	while keep_going:
		seats, keep_going = do_round(seats)

	n_occupied = 0
	for y in range(1, len(seats)-1):
		for x in range(1, len(seats[0])-1):
			n_occupied += int(seats[y][x] == OCCUPIED)

	print(n_occupied)