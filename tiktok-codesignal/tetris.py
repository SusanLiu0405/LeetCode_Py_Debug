def solution(n, m, figures):
    g = [[0]*m for _ in range(n)]
    s = {
        'A': [(0, 0)],
        'B': [(0, 0), (0, 1), (0, 2)],
        'C': [(0, 0), (0, 1), (1, 0), (1, 1)],
        'D': [(0, 0), (1, 0), (2, 0), (1, 1)],
        'E': [(0, 1), (1, 0), (1, 1), (1, 2)],
    }
    for v, ch in enumerate(figures, 1):
        for r in range(n):
            for c in range(m):
                if all(0 <= r+dr < n and 0 <= c+dc < m and not g[r+dr][c+dc] for dr, dc in s[ch]):
                    for dr, dc in s[ch]:
                        g[r+dr][c+dc] = v
                    r = c = n
                    break
    return g
