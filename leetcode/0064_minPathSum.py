'''
本题与滚雪球相同。
'''
def get_min_path(matrix):
	rows = len(matrix)
	cols = len(matrix[0])
	for row in range(rows):
		for col in range(cols):
			min_value = float('inf')
			if row > 0:
				min_value = min(matrix[row - 1][col], min_value)
			if col > 0:
				min_value = min(matrix[row][col - 1], min_value)
			# print(up, left)
			if min_value == float('inf'):
				matrix[row][col] = matrix[row][col]
			else:
				matrix[row][col] += min_value
	# print(matrix)
	return matrix[rows - 1][cols - 1]

input_matrix = [
	[0, 1, 2],
	[3, 4, 5],
	[6, 7, 8]]
print(get_min_path(input_matrix))

# def get_min_sum_dfs(matrix):
#     result = [float('inf')]
#     dfs(0, 0, matrix, 0, result)
#     return result[0]

# def dfs(r, c, matrix, sum, result):
#     if r == len(matrix) or c == len(matrix[0]):
#         return
#     sum += matrix[r][c]

#     # reached the bottom right corner:
#     if r == len(matrix) - 1 and c == len(matrix[0]) - 1:
#         result[0] = min(result[0], sum)
#         return

#     # go down, go right
#     dfs(r + 1, c, matrix, sum, result)
#     dfs(r, c + 1, matrix, sum, result)
# print(get_min_sum_dfs(input_matrix))
