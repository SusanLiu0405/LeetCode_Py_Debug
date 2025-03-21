# from collections import Counter
#
# def maximumLikes(prediction):
# 	if not prediction:
# 		return 0
#
# 	trends = group_trends(prediction)
# 	n = len(trends)
# 	if n == 1:
# 		return trends[0]
#
# 	dp = [0] * n
# 	dp[0] = trends[0]
# 	dp[1] = max(trends[0], trends[1])
#
# 	for i in range(2, n):
# 		dp[i] = max(dp[i-1], dp[i-2] + trends[i])
# 	return dp[-1]
#
#
# def group_trends(prediction):
# 	frequency = Counter(prediction)
# 	result = []
# 	for i in range(1, len(frequency) + 1):
# 		if frequency[i] > 0:
# 			result.append(i * frequency[i])
# 	return result
#
# prediction = [1, 1, 1]
# print(group_trends(prediction))
# print(maximumLikes(prediction))


def maximumLikes(prediction):
	from collections import Counter
	freq = Counter(prediction)

	if not prediction:
		return 0

	max_num = max(prediction)  # largest trend
	dp = [0] * (max_num + 1)

	for i in range(1, max_num + 1):
		if i == 1:
			dp[i] = i * freq[i]
		else:
			dp[i] = max(dp[i - 1], dp[i - 2] + i * freq[i])

	return dp[max_num]

prediction = [1, 2, 3, 3, 3, 4, 4]
print(maximumLikes(prediction))