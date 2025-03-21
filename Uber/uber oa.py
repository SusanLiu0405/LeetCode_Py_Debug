'''
https://docs.google.com/document/d/1_oGthQmK7Iz8ky3qrvpZul8BpFUQRCiodcDlfZR47BQ/edit?tab=t.0
'''


# codesignal bullshit

# Q1 in doc (Z)
def solution(arr):
	for i in range(len(arr) // 2):
		left_index = i * 2
		right_index = i * 2 + 1
		if arr[left_index] > arr[right_index]:
			arr[left_index], arr[right_index] = arr[right_index], arr[left_index]
	return arr


# Q2 (Rich) Richard is examining your Q2 answer, if he is good with it, then we are done
# no, it should be modified. the question in the doc is not the same.
# done
# wait what was Q2
# i think i saw Q1 and thought it was Q2


# ok susan, fucking rich does not read your solution, he wrote his own, you can comment out your solution, and add rich's solution

# def solution(arr):
#     n = len(arr)
#     for i in range(0, n - 1, 2):
#         if arr[i] > arr[i + 1]:
#             arr[i], arr[i + 1] = arr[i + 1], arr[i]

#     return arr

# all good?? then submit~~~~~
# make sure camera is off before talking
# they will send back score and grading rubric
# okay I will keep an eye on that
# Thank you guys!

def time_to_minutes(time_str):
	hours, minutes = time_str.split(':')
	return (int(hours) * 60) + int(minutes)


def minutes_to_time(minutes):
	hours = minutes // 60
	minutes %= 60
	return f'{hours:02}:{minutes:02}'


# will shuttle_times be sorted?
# not sure, but i think yes
# turn off your audio rich ....
# remember: no bus coming
# dont wait 24 hours for the next one?
# no, if no coming bus, return -1
# my only change was to sort the shuttle times
def solution(shuttle_times, current_time):
	current_min = time_to_minutes(current_time)
	shuttle_minutes = [time_to_minutes(shuttle_time) for shuttle_time in shuttle_times]
	shuttle_minutes.sort()
	for shuttle_min in shuttle_minutes:
		if shuttle_min >= current_min:
			wait_min = shuttle_min - current_min
			return minutes_to_time(wait_min)

	return -1


# allpass!


# Q3 (Rich)
# Q3 passed! Rich can you see
def align_center(line, width):
	spaces_needed = width - len(line)
	left_padding = spaces_needed // 2
	right_padding = spaces_needed - left_padding
	return '*' + (' ' * left_padding) + line + (' ' * right_padding) + '*'


def solution(paragraphs, width):
	asterisks = '*' * (width + 2)
	res = [asterisks]
	for paragraph in paragraphs:
		line = ''

		for word in paragraph:
			if len(line) + len(word) + (1 if line else 0) > width:
				res.append(align_center(line, width))
				line = word
			else:
				if line:
					line += ' '
				line += word
		if line:
			res.append(align_center(line, width))

	res.append(asterisks)
	return res


# include this Comment
# What happens if the width is less than the width of a word in the paragraph?

# Q4 (Z)

def solutoin(rates, strategy, k):
	total = 0
	length = len(rates)

	for i in range(length):
		total += strategy[i] * rates[i]

	max_total = total

	# k <= length
	for i in range(k):
		# reverse the value in total
		total += -1 * strategy[i] * rates[i]
		if k // 2 <= i < k:
			total += 1 * rates[i]

	max_total = max(max_total, total)

	for i in range(1, length - k + 1):
		# left most
		left_index = i - 1
		# Count in left most original
		total += strategy[left_index] * rates[left_index]

		# middle
		mid_index = i + k // 2 - 1
		# remove middle as 1
		total += -1 * 1 * rates[mid_index]

		# reverse right most
		right_index = i + k - 1
		# remove right most original
		total += -1 * strategy[right_index] * rates[right_index]
		# Count in right most as strategy 1
		total += 1 * rates[right_index]

		max_total = max(max_total, total)

	return max_total

