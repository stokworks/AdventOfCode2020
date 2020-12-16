#! /usr/bin/env python

import re
import sys

RULE_PATTERN = re.compile(r'^([\w ]+): (\d+)-(\d+) or (\d+)-(\d+)$')

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
				
	valid_tickets = list(filter(
		lambda ticket: all([value < len(num_to_rule) and len(num_to_rule[value]) > 0 for value in ticket]),
		nearby_tickets))

	ticket_possibilities = [[num_to_rule[value].copy() for value in ticket] for ticket in valid_tickets]

	names = [rules[i][0] for i in range(0, len(rules), 2)]
	name_to_columns = {name:set() for name in names}

	for try_name in names:
		col_ind = None
		for col in range(len(ticket_possibilities[0])):
			col_possible = True
			for ticket in ticket_possibilities:
				if not try_name in ticket[col]:
					col_possible = False
					break
			if col_possible:
				name_to_columns[try_name].add(col)

	name_to_column = {}
	used_columns = set()
	unused_names = names.copy()

	while len(unused_names) > 0:
		name = unused_names.pop(0)
		possible_columns = name_to_columns[name] - used_columns
		if len(possible_columns) == 1:
			column = possible_columns.pop()
			name_to_column[name] = column
			used_columns.add(column)
		else:
			unused_names.append(name)
	
	departure_values = 1
	for name, column in name_to_column.items():
		if name[:len('departure')] == 'departure':
			departure_values *= your_ticket[column]

	print(departure_values)