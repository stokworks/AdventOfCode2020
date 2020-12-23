#! /usr/bin/env python

import copy
import sys

from pyparsing import *

expr = infixNotation(
	pyparsing_common.integer,
	[
		(oneOf('+ *'), 2, opAssoc.LEFT)
	],
)

def evaluate(tree):
	if isinstance(tree, int):
		return tree
	elif isinstance(tree, list):
		if len(tree) == 1:
			return evaluate(tree[0])
		elif len(tree) >= 3:
			if tree[-2] == '+':
				return evaluate(tree[:-2]) + evaluate(tree[-1])
			elif tree[-2] == '*':
				return evaluate(tree[:-2]) * evaluate(tree[-1])
		else:
			print('Unexpected tree length: {}'.format(len(tree)))
	else:
		print('Unexpected tree type: {}'.format(tree.__class__.__name__))


if __name__ == '__main__':
	es = []
	with open(sys.argv[1]) as f:
		es = [line.strip() for line in f]

	total = 0
	for e in es:
		total += evaluate(expr.parseString(e).asList())
	print(total)