def group_trends(prediction):
	if not prediction:
		return []
	result = [prediction[0]]

	for i in range(1, len(prediction)):
		if prediction[i - 1] > prediction[i]:
			result.append(prediction[i])
		else:
			result[-1] += prediction[i]
	return result

def maximumLikes(prediction):
	if not prediction:
		return 0
	trends = group_trends(prediction)

	n = len(trends)
	if n == 1:
		return trends[0]

	dp = [0] * n
	dp[0] = trends[0]
	dp[1] = max(trends[0], trends[1])
	for i in range(2, n):
		dp[i] = max(dp[i - 1], dp[i - 2] + trends[i])
	return dp[n - 1]

test_predictions = [
		[1, 3, 1, 4],
		[1, 2, 3, 4, 5],
		[1, 1, 2, 2, 3, 3, 4, 4],
		[1, 1, 0, 1, 3, 4],
		[1, 3, 1, 4, 1, 5, 1, 6],
		[1, 1, 2, 3, 5, 8],
		[20000, 20000],
		[20000, 19000],
		[5],
		[5, 4, 3, 2, 1],
		[2, 2, 3, 2, 2, 2, 5, 5, 4, 4, 6],
		[99999, 100000, 99999, 100000, 99998],
		[5, 5, 5, 5, 5],
		[10, 9, 9, 10, 10, 9, 0, 1, 2, 2, 1, 5]

	]
for p in test_predictions:
	print("\nPrediction:", p)
	trends = group_trends(p)
	print("Grouped Trends:",trends)
	print("maximum likes:", maximumLikes(trends))
