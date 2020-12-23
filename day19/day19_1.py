#! /usr/bin/env python

import re
import sys

def parse_rule(rule_txt):
	rule_num = int(rule_txt[:rule_txt.index(':')])
	options = rule_txt[rule_txt.index(':') + 2:].split('|')

	if options[0][0] == '"':
		options = options[0][1]
	elif len(options) == 1:
		options = list(map(int, options[0].split(' ')))
	else:
		options = (
			list(map(int, options[0].strip().split(' '))),
			list(map(int, options[1].strip().split(' ')))
		)

	return (rule_num, options)

class RuleTree:
	def __init__(self):
		self.num = None
		self.left = []
		self.right = []
		self.literal = None

	def fully_matches(self, string):
		matches = self.parse_string(string)
		return any([len(m[1]) == 0 for m in matches])

	def parse_string(self, string):
		options = []
		if self.literal:
			l = len(self.literal)
			if len(string) < l:
				return []
			elif string[:l] == self.literal:
				return [(string[:l], string[l:])]
			else:
				return []

		# improvement: combine options of equal length?
		if self.left:
			options.extend(self.parse_sequence(self.left, string))
		if self.right:
			options.extend(self.parse_sequence(self.right, string))

		return options

	def parse_sequence(self, sequence, string):
		seq_todo = sequence.copy()
		options = [('', string)]
		for part in sequence:
			new_options = []
			for opt_matched, opt_leftover in options:
				result = part.parse_string(opt_leftover)
				for matched, leftover in result:
					new_options.append((opt_matched + matched, leftover))
			options = new_options

		if len(options) == 1 and options[0][1] == string:
			options = []
		return options

	def parse_sub(self, sub, string):
		return sub.parse_string(string)

	def __str__(self):
		output = '(({})'.format(self.num)
		if self.left:
			output += ' [' + ', '.join([str(sub) for sub in self.left]) + ']'
		if self.right:
			output += ' | [' + ', '.join([str(sub) for sub in self.right]) + ']'
		if self.literal:
			output += ' "' + self.literal + '"'
		output += ')'
		return output
			
if __name__ == '__main__':
	with open(sys.argv[1]) as f:
		c = f.read()
		rules = [parse_rule(l.strip()) for l in c.split('\n\n')[0].split('\n')]
		messages = [l.strip() for l in c.split('\n\n')[1].split('\n')]

	rule_dict = dict()

	# create node for each rule
	for r in rules:
		node = RuleTree()
		node.num = r[0]
		if isinstance(r[1], str):
			node.literal = r[1]
		elif isinstance(r[1], list):
			node.left = r[1]
		elif isinstance(r[1], tuple):
			node.left = r[1][0]
			node.right = r[1][1]
		rule_dict[r[0]] = node

	# create tree
	for rule_num, rule in rule_dict.items():
		if rule.left:
			rule.left = [rule_dict[sub_num] for sub_num in rule.left]
		if rule.right:
			rule.right = [rule_dict[sub_num] for sub_num in rule.right]

	root = rule_dict[0]

	n = 0
	for message in messages:
		n += int(root.fully_matches(message))
	print(n)
