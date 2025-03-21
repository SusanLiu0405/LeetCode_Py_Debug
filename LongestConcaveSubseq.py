def get_longest_concave_subseq(arr):
    if len(arr) == 1:
        return 1
    else:
	    return max(get_longest_concave_subseq_one_direction(arr), get_longest_concave_subseq_one_direction(arr[::-1]))


def get_longest_concave_subseq_one_direction(arr):
	num_cnt = [0] * (len(arr) + 1)
	visited_nums = set()
	max_length = 0
	for num in arr:
		for visited_num in visited_nums:
			if num < visited_num:
				num_cnt[visited_num] += 1
			else:
				max_length = max(max_length, num_cnt[visited_num] + 2)

		visited_nums.add(num)
	# print(max_length)
	return max_length


print(get_longest_concave_subseq([4, 2, 6, 5, 3, 1]))  # 3
print(get_longest_concave_subseq([3, 2, 1]))  # 3
print(get_longest_concave_subseq([2, 3, 1]))  # 3
print(get_longest_concave_subseq([1, 2]))  # 3
print(get_longest_concave_subseq([2, 1]))  # 3
print(get_longest_concave_subseq([2, 2, 2]))  # 3
print(get_longest_concave_subseq([6, 6, 6, 6, 6, 6]))  # 3
print(get_longest_concave_subseq([5, 1, 1, 1, 5]))  # 3
print(get_longest_concave_subseq([1]))  # 3
