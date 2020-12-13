#! /usr/bin/env python

import copy
import sys

NONE = '.'
EMPTY = 'L'
OCCUPIED = '#'

class Seat:
	def __init__(self):
		self.type = EMPTY
		self.neighbours = set()
		self.adjecent = 0

	def add_neighbour(self, other):
		self.neighbours.add(other)

	def count_adjecent(self):
		self.adjecent = 0
		for other in self.neighbours:
			self.adjecent += int(other.type == OCCUPIED)
		return self.adjecent


	def __str__(self):
		return self.type

def generate_seats(floorplan):
	seats = []
	for y in range(len(floorplan)):
		row = []
		for x in range(len(floorplan[0])):
			if floorplan[y][x] == EMPTY:
				row.append(Seat())
			else:
				row.append(None)
		seats.append(row)

	for y in range(len(seats)):
		for x in range(len(seats[0])):
			if seats[y][x]:
				find_neighbours(seats, x, y)

	return seats

def find_neighbours(seats, x, y):
	for dx in range(-1, 2):
		for dy in range(-1, 2):
			if dx == 0 and dy == 0:
				continue
			else:
				other = find_neighbour(seats, x, y, dx, dy)
				if other:
					seats[y][x].add_neighbour(other)

def find_neighbour(seats, x, y, dx, dy):
	dist = 1
	while True:
		ox = x + dx * dist
		oy = y + dy * dist

		if oy < 0 or oy >= len(seats) or ox < 0 or ox >= len(seats[0]):
			return None

		other = seats[oy][ox]
		if other:
			return other

		dist += 1

def do_round(seats):
	changed = False

	for y in range(len(seats)):
		for x in range(len(seats[0])):
			seat = seats[y][x]
			if not seat:
				continue
			seat.count_adjecent()

	for y in range(len(seats)):
		for x in range(len(seats[0])):
			seat = seats[y][x]
			if not seat:
				continue

			if seat.type == EMPTY and seat.adjecent == 0:
				seat.type = OCCUPIED
				changed = True
			elif seat.type == OCCUPIED and seat.adjecent >= 5:
				seat.type = EMPTY
				changed = True

	return seats, changed

def print_seats(seats):
	print('\n'.join([''.join([str(seat) if seat else NONE for seat in row]) for row in seats]))
	print()

if __name__ == '__main__':
	floorplan = []
	with open(sys.argv[1]) as f:
		for l in f:
			floorplan.append(l.strip())

	seats = generate_seats(floorplan)

	keep_going = True
	while keep_going:
		# print_seats(seats)
		seats, keep_going = do_round(seats)

	n_occupied = 0
	for y in range(len(seats)):
		for x in range(len(seats[0])):
			if not seats[y][x]:
				continue
			n_occupied += int(seats[y][x].type == OCCUPIED)

	print(n_occupied)
