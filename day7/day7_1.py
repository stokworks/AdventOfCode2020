#! /usr/bin/env python

import re
import sys

LOOKING_FOR = 'shiny gold'

if __name__ == '__main__':
	rule_re = re.compile(r'([\w ]+?) bags contain (.+)\.')
	content_re = re.compile(r'(\d+|no) ([\w ]+) bags?')

	is_in = dict()

	with open(sys.argv[1]) as f:
		txt = f.read()

		for rule in re.finditer(rule_re, txt):
			container = rule.group(1)
			rest = rule.group(2)

			for content in re.finditer(content_re, rest):
				amount = content.group(1)
				color = content.group(2)

				if color in is_in:
					is_in[color].append(container) 
				else:
					is_in[color] = [container]

	queue = is_in[LOOKING_FOR]
	containers = set()

	while len(queue):
		elem = queue.pop()
		containers.add(elem)
		queue.extend(is_in[elem] if elem in is_in else [])

	print(len(containers))