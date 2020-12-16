#! /usr/bin/env python

import re
import sys

RULE_PATTERN = re.compile(r'(\w+): (\d+)-(\d+) or (\d+)-(\d+)')

def read_rules(rules_txt):
	rules = []
	for rule_txt in rules_txt:
		name, r0s, r0e, r1s, r1e = RULE_PATTERN.search(rule_txt).groups()
		r0s, r0e, r1s, r1e = int(r0s), int(r0e), int(r1s), int(r1e)
		rules.append((name, r0s, r0e))
		rules.append((name, r1s, r1e))
	return rules

def read_tickets(tickets_txt):
	return [list(map(int, ticket_txt.split(','))) for ticket_txt in tickets_txt]

if __name__ == '__main__':
	with open(sys.argv[1]) as f:
		parts = [l.strip().split('\n') for l in f.read().split('\n\n')]
		parts[1].pop(0)
		parts[2].pop(0)

	rules = read_rules(parts[0])
	your_ticket    = read_tickets(parts[1])[0]
	nearby_tickets = read_tickets(parts[2])

	num_to_rule = []
	for i in range(max([range_end for _, _, range_end in rules]) + 1):
		num_to_rule.append([])
	for name, range_start, range_end in rules:
		for i in range(range_start, range_end + 1):
			num_to_rule[i].append(name)

	for ticket in nearby_tickets:
		for value in ticket:
			if value >= len(num_to_rule) or len(num_to_rule[value]) == 0:
				error_rate += value
	print(error_rate)