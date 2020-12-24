#! /usr/bin/env python

import sys

ROUNDS = 10000000
MAX_CUP = 1000000

class Linked:
	def __init__(self, val):
		self.val = val
		self.prev = None
		self.next = None

	def find_cup(self, val):
		# better make sure val is in there
		if self.val == val:
			return self
		else:
			return self.next.find_cup(val)

	def __str__(self):
		return str(self.val) + self.next.to_string(self.val)

	def to_string(self, start):
		if self.val == start:
			return ''
		else:
			return str(self.val) + self.next.to_string(start)

if __name__ == '__main__':
	cups_txt = '315679824'

	cups = [Linked(int(v)) for v in cups_txt]
	min_cup = min([int(v) for v in cups_txt])
	max_cup = max([int(v) for v in cups_txt])

	for i in range(max_cup + 1, MAX_CUP + 1):
		cups.append(Linked(i))

	max_cup = MAX_CUP

	for i, c in enumerate(cups):
		if i == 0:
			c.prev = cups[-1]
			c.next = cups[i+1]
		elif i == len(cups) - 1:
			c.prev = cups[i-1]
			c.next = cups[0]
		else:
			c.prev = cups[i-1]
			c.next = cups[i+1]

	by_val = [None] * (len(cups) + 1)
	for c in cups:
		by_val[c.val] = c

	current_cup = cups[0]

	for i in range(ROUNDS):
		# pick up three cups
		pick_up = current_cup.next
		current_cup.next = pick_up.next.next.next
		pick_up.next.next.next.prev = current_cup
		pick_up.prev = None
		pick_up.next.next.next = None
		# pick destination cup
		try_destination = current_cup.val - 1
		while try_destination in [pick_up.val, pick_up.next.val, pick_up.next.next.val] or try_destination < min_cup:
			try_destination -= 1
			if try_destination < min_cup:
				try_destination = max_cup
		# put down cups
		destination = by_val[try_destination]
		pick_up.prev = destination
		pick_up.next.next.next = destination.next
		destination.next.prev = pick_up.next.next.next
		destination.next = pick_up
		# pick current cup
		current_cup = current_cup.next

	cup1 = by_val[1]
	print(cup1.next.val * cup1.next.next.val)