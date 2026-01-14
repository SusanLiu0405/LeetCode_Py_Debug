def getMinimumTotalCost(videoChunks, k):
	fixed_cost = videoChunks[0] + videoChunks[-1]
	tbd_cost = []

	for i in range(len(videoChunks) - 1):
		tbd_cost.append(videoChunks[i] + videoChunks[i + 1])

	tbd_cost.sort()
	final_cost = fixed_cost + sum(tbd_cost[0:k - 1])

	return final_cost
if __name__ == '__main__':
	videoChunks = [9, 8, 3, 4, 2, 7]
	k = 1
	print(getMinimumTotalCost(videoChunks, k))