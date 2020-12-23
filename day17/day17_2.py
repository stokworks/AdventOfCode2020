#! /usr/bin/env python

import copy
import sys

N_ROUNDS = 6
INACTIVE = '.'
ACTIVE = '#'

def count_adjecent(cubes, w, z, y, x):
	n = 0
	for dw in range(-1, 2):
		for dz in range(-1, 2):
			for dy in range(-1, 2):
				for dx in range(-1, 2):
					if dw == 0 and dz == 0 and dy == 0 and dx == 0:
						continue
					if w + dw < 0 or w + dw >= len(cubes):
						continue
					if z + dz < 0 or z + dz >= len(cubes[w + dw]):
						continue
					if y + dy < 0 or y + dy >= len(cubes[w + dw][z + dz]):
						continue
					if x + dx < 0 or x + dx >= len(cubes[w + dw][z + dz][y + dy]):
						continue
					n += int(cubes[w + dw][z + dz][y + dy][x + dx])
	return n

def do_round(cubes):
	new_cubes = copy.deepcopy(cubes)
	for w in range(len(cubes)):
		for z in range(len(cubes[w])):
			for y in range(len(cubes[w][z])):
				for x in range(len(cubes[w][z][y])):
					n = count_adjecent(cubes, w, z, y, x)
					if cubes[w][z][y][x] and (n < 2 or n > 3):
						new_cubes[w][z][y][x] = False
					elif not cubes[w][z][y][x] and n == 3:
						new_cubes[w][z][y][x] = True
	return new_cubes

def grow_cubes(cubes):
	# grow w dimension
	cubes.insert(0, [[[False 
		for x in range(len(cubes[0][z][y]))] 
		for y in range(len(cubes[0][z]))] 
		for z in range(len(cubes[0]))])
	cubes.append([[[False 
		for x in range(len(cubes[0][z][y]))] 
		for y in range(len(cubes[0][z]))] 
		for z in range(len(cubes[0]))])

	# grow z dimension
	for w in range(len(cubes)):
		cubes[w].insert(0,[[False 
			for x in range(len(cubes[w][0][y]))] 
			for y in range(len(cubes[w][0]))])
		cubes[w].append([[False 
			for x in range(len(cubes[w][0][y]))] 
			for y in range(len(cubes[w][0]))])

	# grow y dimension
	for w in range(len(cubes)):
		for z in range(len(cubes[w])):
			cubes[w][z].insert(0, [False
				for x in range(len(cubes[w][z][0]))])
			cubes[w][z].append([False
				for x in range(len(cubes[w][z][0]))])

	# grow x dimension
	for w in range(len(cubes)):
		for z in range(len(cubes[w])):
			for y in range(len(cubes[w][z])):
				cubes[w][z][y].insert(0, False)
				cubes[w][z][y].append(False)

	return cubes

if __name__ == '__main__':
	z_0 = []
	with open(sys.argv[1]) as f:
		for l in f:
			z_0.append([True if c == ACTIVE else False for c in list(l.strip())])

	cubes = [[z_0]]

	for _ in range(N_ROUNDS):
		cubes = grow_cubes(cubes)
		cubes = do_round(cubes)
	
	n = 0
	for w in range(len(cubes)):
		for z in range(len(cubes[w])):
			for y in range(len(cubes[w][z])):
				for x in range(len(cubes[w][z][y])):
					n += int(cubes[w][z][y][x])
	print(n)