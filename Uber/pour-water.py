from collections import deque

def water_flow(height, startrow, startcol):
    rows, cols = len(height), len(height[0])
    output = [[-1] * cols for _ in range(rows)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 4 directions

    # initialize the queue and start point
    queue = deque([(startrow, startcol, 0)])
    output[startrow][startcol] = 0

    while queue:
        r, c, time = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if output[nr][nc] == -1 and height[nr][nc] <= height[r][c]:
                    output[nr][nc] = time + 1
                    queue.append((nr, nc, time + 1))

    return output


height = [[10, 11, 10],
          [ 4,  0,  6],
          [ 3,  2,  1]]
startrow, startcol = 1, 1
result = water_flow(height, startrow, startcol)
for row in result:
    print(row)
