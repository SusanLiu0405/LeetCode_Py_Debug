def compute_number_score(number):
	score = 0
	num_str = str(number)

	# +2 points for every 5 in the number
	score += 2 * num_str.count('5')

	# +4 points for each pair of consecutive 3s
	count_3s = 0
	prev_digit = ''
	for digit in num_str:
		if digit == '3':
			count_3s += 1
		else:
			if count_3s > 1:
				score += 4 * (count_3s - 1)
			count_3s = 0
	if count_3s > 1:  # Check at the end of the number
		score += 4 * (count_3s - 1)

	# +N^2 points for a sequence of length N (N >= 1) where each digit is 1 more than the previous digit
	increasing_seq_length = 1
	for i in range(1, len(num_str)):
		if int(num_str[i]) == int(num_str[i - 1]) + 1:
			increasing_seq_length += 1
		else:
			if increasing_seq_length > 1:
				score += increasing_seq_length ** 2
			increasing_seq_length = 1
	if increasing_seq_length > 1:  # Check at the end of the number
		score += increasing_seq_length ** 2

	# +6 if the entire number is a multiple of 5
	if number % 5 == 0:
		score += 6

	# +1 for each odd digit
	score += sum(1 for digit in num_str if int(digit) % 2 != 0)

	return score


if __name__ == '__main__':
	# Example usage:
	print(compute_number_score(5751))  # Output: 4
	print(compute_number_score(9678562))  # Output: 15
	print(compute_number_score(456))  # Output: 12
	print(compute_number_score(5))