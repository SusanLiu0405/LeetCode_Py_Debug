# def spiralmatrix(matrix):
#     m = len(matrix)
#     n = len(matrix[0])
#     top = 0
#     down = m - 1
#     left = 0
#     right = n - 1
#     result = []

#     # right, down, left, up
#     while top <= down and left <= right:
#         for i in range(left, right + 1):
#             result.append(matrix[top][i])
#         top += 1
#         for i in range(top, down + 1):
#             result.append(matrix[i][right])
#         right -= 1
#         if top <= down:
#             for i in range(right, left - 1, -1):
#                 result.append(matrix[down][i])
#             down -= 1
#         if left <= right:
#             for i in range(down, top - 1, -1):
#                 result.append(matrix[i][left])
#             left += 1
#     return result

# matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# print(spiralmatrix(matrix))

# # matrix = [[1,2,3],[4,5,6],[7,8,9]]
# # print(spiralmatrix(matrix))

# '''
# top = 0
# down = 2
# left = 0
# right = 2
# i in 0, 1, 2
# 0, 0
# 0, 1
# 0, 2
# top = 1
# down = 2
# left = 0
# right = 2
# i = 1, 2
# 1, 2
# 2, 2

# top = 1
# down = 2
# left = 0
# right = 1
# i = 1, 0
# 2, 1
# 2, 0

# top = 1
# down = 1
# left = 0
# right = 1

# i = 1, 0
# 1, 0
# '''

'''
Example1:
Input: n = 3 Output: ["((()))","(()())","(())()","()(())","()()()"]
            l=0 r=0
            /    
            l=1 r=0
           /      \
        l=2 r=0   l=1 r=1
        /    \
    l=3, r=0.  l=2, r=1
'''
def recursion(left, right, result):
    left = 0
    right = 0
    



