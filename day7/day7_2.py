#! /usr/bin/env python

import re
import sys

LOOKING_FOR = 'shiny gold'

if __name__ == '__main__':
	rule_re = re.compile(r'([\w ]+?) bags contain (.+)\.')
	content_re = re.compile(r'(\d+|no) ([\w ]+) bags?')

	bags = dict()
	is_in = dict()

	with open(sys.argv[1]) as f:
		txt = f.read()

		for rule in re.finditer(rule_re, txt):
			container = rule.group(1)
			rest = rule.group(2)

			bags[container] = []

			for content in re.finditer(content_re, rest):
				amount = content.group(1)
				color = content.group(2)
				
				if amount != 'no':
					bags[container].append({ 
						'amount': int(amount), 
						'color': color
					})

				if color in is_in:
					is_in[color].append(container) 
				else:
					is_in[color] = [container]

	queue = list(filter(lambda color: len(bags[color]) == 0, bags.keys()))
	num_sub_bags = dict()
	
	while len(queue):
		elem = queue.pop(0)
		contained_by = is_in[elem] if elem in is_in else []
		contains = bags[elem]

		if not elem in num_sub_bags:
			if len(contains) == 0:
				num_sub_bags[elem] = 0
				queue.extend(contained_by)
			elif all(sub_bag['color'] in num_sub_bags for sub_bag in contains):
				num_sub_bags[elem] = 0
				for sub_bag in contains:
					num_sub_bags[elem] += sub_bag['amount'] * (num_sub_bags[sub_bag['color']] + 1)
				queue.extend(contained_by)

				if elem == 'shiny gold':
					break
			else:
				queue.append(elem)
	
	print(num_sub_bags['shiny gold'])