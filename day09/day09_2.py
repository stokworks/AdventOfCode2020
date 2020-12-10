#! /usr/bin/env python

import sys

if __name__ == '__main__':
	PREAMBLE_SIZE = int(sys.argv[1])

	with open(sys.argv[2]) as f:
		nums = [int(n.strip()) for n in f]

	i_invalid = None
	n_invalid = None

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
			i_invalid = i
			n_invalid = nums[i]
			break

	for window_size in range(1, len(nums)):
		for i_start in range(0, len(nums) - window_size):
			if i_start <= i_invalid and i_invalid < i_start + window_size:
				continue

			smallest = None
			largest = None
			window_sum = 0
			window = nums[i_start:i_start + window_size]

			for n in window:
				if not smallest or n < smallest:
					smallest = n
				if not largest or n > largest:
					largest = n
				window_sum += n

			if window_sum == n_invalid:
				print(smallest + largest)
				sys.exit()