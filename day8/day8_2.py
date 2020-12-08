#! /usr/bin/env python

import sys

def terminates(prog):
	acc = 0
	pc = 0
	visited = [False] * len(prog)

	while pc < len(prog) and not visited[pc]:
		visited[pc] = True
		inst, num = prog[pc]
		if inst == 'acc':
			acc += num
		elif inst == 'jmp':
			pc += num - 1
		
		pc += 1

	if pc == len(prog):
		return (True, acc)
	else:
		return (False, acc)

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

	for i in range(len(prog)):
		if prog[i][0] == 'acc':
			continue

		new_prog = prog.copy()
		inst, num = new_prog[i]
		new_prog[i] = ('nop', num) if inst == 'jmp' else ('jmp', num)
		terms, acc = terminates(new_prog)

		if (terms):
			print(acc)
			break