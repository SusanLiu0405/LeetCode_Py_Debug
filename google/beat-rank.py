'''
给定 n 个选手，真实排名为 1 ~ n 且唯一。已知规则是：排名高的人一定能赢排名低的人。但具体排名未知。
给定 m 场比赛结果(a beat b)表示 a 一定比 b 强。
问题：
找出所有排名可以被唯一确定的选手，并给出他们的排名。
Solution: 建一个有向图 然后对原图统计weaker 反图统计stronger，如果有player的weaker+stronger=n-1，就算知道这个player的rank

[[1, 2], [1, 3], [3, 4]]
n = 4
'''
from collections import deque
class Solution:
    def beat_rank(self, match, n):
        result = {}
        graph = [[] for _ in range(n + 1)]
        reverse_graph = [[] for _ in range(n + 1)]
        for i in range(len(match)):
            winner, loser = match[i]
            graph[winner].append(loser)
            reverse_graph[loser].append(winner)

        for i in range(1, n + 1):
            beated = self.bfs(graph, n, i)
            stronger = self.bfs(reverse_graph, n, i)
            if stronger + beated + 1 == n:
                rank = stronger + 1
                result[i] = rank
        return result
        
    
    def bfs(self, graph, n, start):
        visited = [False] * (n + 1)
        dq = deque()
        visited[start] = True
        dq.append(start)
        beated = 0
        while dq:
            curr = dq.popleft()
            for next in graph[curr]:
                if visited[next] == True:
                    continue
                visited[next] = True
                dq.append(next)
                beated += 1
        return beated

sol = Solution()
match = [[1, 2], [2, 3], [4, 3]]
n = 4
print(sol.beat_rank(match, 4))