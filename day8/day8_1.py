#! /usr/bin/env python

import sys

if __name__ == '__main__':
	prog = []

	with open(sys.argv[1]) as f:
		for i in f:
			i = i.strip()
			inst = i[:3]
			sign = i[4]
			num = int(i[5:])
			num = num if sign == '+' else -num
			prog.append((inst, num))
	
	acc = 0
	pc = 0
	visited = [False] * len(prog)

	while not visited[pc]:
		visited[pc] = True
		inst, num = prog[pc]
		if inst == 'acc':
			acc += num
		elif inst == 'jmp':
			pc += num - 1
		
		pc += 1

	print(acc)