# 输入：
# 2 3
# 1 1 1
# 1 1 1
# 输出：
# 行数: 2
# 列数: 3
# 二维数组: [[1, 1, 1], [1, 1, 1]]

# 读取包含行数和列数的第一行
row, col = map(int, input().split())

# 初始化一个二维数组
matrix = []

# 读取剩下的行并将每一行的数字分割并存储到二维数组中
for _ in range(row):
    row_values = list(map(int, input().split()))
    matrix.append(row_values)

# 输出结果
print("行数:", row)
print("列数:", col)
print("二维数组:", matrix)

# 从键盘读取输入：
# [[1,1,0,0,0],
# [0,1,0,1,1],
# [0,0,0,1,1],
# [0,0,0,0,0],
# [0,0,1,1,1]]
grid = []
while True:
    try:
        row1 = list(map(int, input().split()))
        if not row1:
            break
        grid.append(row1)
    except EOFError:
        break

