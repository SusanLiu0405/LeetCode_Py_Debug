def findMinimumInfluencers(influencers, followers):
    import sys
    sys.setrecursionlimit(10**7)
    all_users = set()
    for inf, fol in zip(influencers, followers):
        if inf != -1:
            all_users.add(inf)
        if fol != -1:
            all_users.add(fol)
    n = max(all_users) if all_users else 0
    adj = [[] for _ in range(n+1)]
    for inf, fol in zip(influencers, followers):
        if inf != -1 and fol != -1:
            adj[inf].append(fol)
    i = 0
    stack = []
    on_stack = [False] * (n+1)
    ind = [-1] * (n+1)
    lowlink = [-1] * (n+1)
    scc_id = [-1] * (n+1)
    cur_scc = 0
    def strongconnect(u):
        nonlocal i, cur_scc
        ind[u] = i
        lowlink[u] = i
        i += 1
        stack.append(u)
        on_stack[u] = True
        for v in adj[u]:
            if ind[v] == -1:
                strongconnect(v)
                lowlink[u] = min(lowlink[u], lowlink[v])
            elif on_stack[v]:
                lowlink[u] = min(lowlink[u], ind[v])
        if lowlink[u] == ind[u]:
            while True:
                v = stack.pop()
                on_stack[v] = False
                scc_id[v] = cur_scc
                if v == u:
                    break
            cur_scc += 1
    for u in all_users:
        if ind[u] == -1:
            strongconnect(u)
    ex = 0
    for u in range(1, n+1):
        if u not in all_users:
            ex += 1
    in_degree = [0] * cur_scc
    for u in all_users:
        for v in adj[u]:
            if scc_id[u] != scc_id[v]:
                in_degree[scc_id[v]] += 1
    indegree0 = sum(1 for d in in_degree if d == 0)
    return indegree0 + ex

if __name__ == "__main__":
    # 一个简单测试：互相关注形成一个环，应该只需要 1 个种子
	influencers = [2, 1, 5, 3 ,4]
	followers = [-1, 5, 3, 5, 3]
print(findMinimumInfluencers(influencers, followers))  # 预期输出: 1
