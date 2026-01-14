'''
TikTok is a widely used social media platform where users can upload short videos and share their content preferences.
Usually, if user A follows user B, then user A is said to be a follower of user B.
Once a user follows someone, TikTok may immediately propagate this information to all users who follow them.

As a brand manager tasked with designing a viral campaign,
your objective is to:
determine the main influencer(s) for your brand.

For this campaign, if a user is neither an influencer nor a follower,
that user must be directly introduced to the viral campaign independently.

You are given an integer n, representing the total number of TikTok users currently on the platform
and, two arrays: `influencers` and `followers`, each of size n.

For each index i, `influencers[i]` represents an influencer
				and `followers[i]` represents the user who follows that influencer.
If followers[i] is −1, it indicates that the corresponding user has no followers.

It is important to note the following:

1. Some users may not have any followers, meaning that for them, `followers[i]` will be −1, indicating that the corresponding user does not follow anyone.
2. There may be mutual follow relationships, i.e., user A may follow user B, and user B may follow user A.
3. Some users might not appear in the `influencers` list but do appear in the `followers` list. In such cases, assume these users neither follow nor influence anyone but are still considered individual TikTok users.
'''

import sys
sys.setrecursionlimit(10**7)


def build_graph(influencers, followers):
    """
    根据 influencers 和 followers 构造图（邻接表）和用户集合。
    返回：
      - all_users: 出现在 influencers 或 followers 中的用户 ID 集合（不含 -1）
      - n: 用户 ID 的最大值
      - adj: 邻接表，adj[u] 为从 u 指向的节点列表
    """
    all_users = set()
    for inf, fol in zip(influencers, followers):
        if inf != -1:
            all_users.add(inf)
        if fol != -1:
            all_users.add(fol)
    # 假设用户 ID 为正整数（0或1开始），取最大 ID
    n = max(all_users) if all_users else 0
    # 构造大小为 n+1 的邻接表（下标 0~n）
    adj = [[] for _ in range(n + 1)]
    for inf, fol in zip(influencers, followers):
        if inf != -1 and fol != -1:
            # 表示粉丝 fol 关注了网红 inf，即 inf -> fol
            adj[inf].append(fol)
    return all_users, n, adj


def tarjan_scc(adj, all_users, n):
    """
    利用 Tarjan 算法求解图的强连通分量（SCC）。
    参数：
      - adj: 邻接表，节点范围 0 ~ n
      - all_users: 集合，表示实际出现过的用户（ID集合）
      - n: 邻接表最大下标
    返回：
      - scc_id: 列表，scc_id[u] 表示节点 u 所属的 SCC 编号
      - num_scc: 强连通分量的总数
    """
    stack = []
    on_stack = [False] * (n + 1)
    indices = [-1] * (n + 1)
    lowlink = [-1] * (n + 1)
    scc_id = [-1] * (n + 1)
    index_counter = [0]  # 用列表封装实现非局部变量
    num_scc = [0]  # 当前 SCC 数量

    def strongconnect(u):
        indices[u] = index_counter[0]
        lowlink[u] = index_counter[0]
        index_counter[0] += 1
        stack.append(u)
        on_stack[u] = True

        for v in adj[u]:
            if indices[v] == -1:
                strongconnect(v)
                lowlink[u] = min(lowlink[u], lowlink[v])
            elif on_stack[v]:
                lowlink[u] = min(lowlink[u], indices[v])

        # 如果 u 是 SCC 的根节点
        if lowlink[u] == indices[u]:
            # 弹出栈中直到 u，形成一个 SCC
            while True:
                v = stack.pop()
                on_stack[v] = False
                scc_id[v] = num_scc[0]
                if v == u:
                    break
            num_scc[0] += 1

    for u in all_users:
        if indices[u] == -1:
            strongconnect(u)

    return scc_id, num_scc[0]


def count_isolated_users(all_users, n):
    """
    统计平台上那些完全没出现在 influencers 和 followers 中的用户数量。
    假设平台上用户的 ID 范围为 1 ~ n（或 0 ~ n，当 n 为最大ID时）。
    此处采用 1~n，遍历 1 到 n。
    """
    isolated = 0
    for u in range(1, n + 1):
        if u not in all_users:
            isolated += 1
    return isolated


def compute_scc_indegree(adj, all_users, scc_id, num_scc):
    """
    在构造的 SCC 凝缩图中统计每个 SCC 的入度。
    返回：
      - in_degree: 长度为 num_scc 的列表，in_degree[i] 为 SCC i 的入度
    """
    in_degree = [0] * num_scc
    for u in all_users:
        for v in adj[u]:
            if scc_id[u] != scc_id[v]:
                in_degree[scc_id[v]] += 1
    return in_degree


def findMinimumInfluencers(influencers, followers):
    """
    计算为了覆盖所有在 influencers/followers 中出现的用户，
    所需的最少直接投放网红数量。
    若平台上用户总数由出现的最大用户ID决定，则对于未出现的用户，
    每个用户都必须单独引入（种子数 +1）。
    """
    # 构造图和所有出现的用户集合
    all_users, n, adj = build_graph(influencers, followers)

    # 求强连通分量（SCC）
    scc_id, num_scc = tarjan_scc(adj, all_users, n)

    # 统计完全孤立的用户（未出现在 influencers 和 followers 中的用户）
    isolated_users = count_isolated_users(all_users, n)

    # 在 SCC 凝缩图中统计入度为 0 的分量数
    in_degree = compute_scc_indegree(adj, all_users, scc_id, num_scc)
    scc_zero_indegree = sum(1 for d in in_degree if d == 0)

    # 最少需要的种子数 = SCC 凝缩图中入度为 0 的分量数 + 孤立用户数
    return scc_zero_indegree + isolated_users


# ---------------- 测试示例 ----------------
if __name__ == "__main__":
    # 一个简单测试：互相关注形成一个环，应该只需要 1 个种子
	influencers = [2, 1, 5, 3 ,4]
	followers = [-1, 5, 3, 5, 3]
	print(findMinimumInfluencers(influencers, followers))  # 预期输出: 3
