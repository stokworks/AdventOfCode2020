#! /usr/bin/env python

import copy
import sys

N_ROUNDS = 6
INACTIVE = '.'
ACTIVE = '#'

def count_adjecent(cubes, z, y, x):
	n = 0
	for dz in range(-1, 2):
		for dy in range(-1, 2):
			for dx in range(-1, 2):
				if dz == 0 and dy == 0 and dx == 0:
					continue
				if z + dz < 0 or z + dz >= len(cubes):
					continue
				if y + dy < 0 or y + dy >= len(cubes[z + dz]):
					continue
				if x + dx < 0 or x + dx >= len(cubes[z + dz][y + dy]):
					continue
				n += int(cubes[z + dz][y + dy][x + dx])
	return n

def do_round(cubes):
	new_cubes = copy.deepcopy(cubes)
	for z in range(len(cubes)):
		for y in range(len(cubes[z])):
			for x in range(len(cubes[z][y])):
				n = count_adjecent(cubes, z, y, x)
				if cubes[z][y][x] and (n < 2 or n > 3):
					new_cubes[z][y][x] = False
				elif not cubes[z][y][x] and n == 3:
					new_cubes[z][y][x] = True
	return new_cubes

def grow_cubes(cubes):
	# grow z dimension
	cubes.insert(0, [[False 
		for x in range(len(cubes[0][y]))] 
		for y in range(len(cubes[0]))])
	cubes.append([[False
		for x in range(len(cubes[0][y]))] 
		for y in range(len(cubes[0]))])

	# grow y dimension
	for z in range(len(cubes)):
		cubes[z].insert(0, [False
			for x in range(len(cubes[z][0]))])
		cubes[z].append([False
			for x in range(len(cubes[z][0]))])

	# grow x dimension
	for z in range(len(cubes)):
		for y in range(len(cubes[z])):
			cubes[z][y].insert(0, False)
			cubes[z][y].append(False)

	return cubes

def print_cubes(cubes):
	output = ''

	for z in range(len(cubes)):
		output += 'z={}\n'.format(z)
		for y in range(len(cubes[z])):
			for x in range(len(cubes[z][y])):
				output += ACTIVE if cubes[z][y][x] else INACTIVE
			output += '\n'

	print(output)

if __name__ == '__main__':
	z_0 = []
	with open(sys.argv[1]) as f:
		for l in f:
			z_0.append([True if c == ACTIVE else False for c in list(l.strip())])

	cubes = [z_0]

	for _ in range(N_ROUNDS):
		cubes = grow_cubes(cubes)
		cubes = do_round(cubes)
	
	n = 0
	for z in range(len(cubes)):
		for y in range(len(cubes[z])):
			for x in range(len(cubes[z][y])):
				n += int(cubes[z][y][x])
	print(n)