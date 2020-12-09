#! /usr/bin/env python

import sys

if __name__ == '__main__':
	PREAMBLE_SIZE = int(sys.argv[1])

	with open(sys.argv[2]) as f:
		nums = [int(n.strip()) for n in f]

	for i in range(PREAMBLE_SIZE, len(nums)):
		window = nums[i-PREAMBLE_SIZE:i]
		found = False

		for j, n1 in enumerate(window):
			for n2 in window[j+1:]:
				if n1 + n2 == nums[i]:
					found = True
					break
			if found:
				break

		if not found:
			print(nums[i])
			break