# def gold_chain_reconnect(weights) -> bool:
#     n = len(weights)
#     if n == 1:
#         return True
#     if n < 3:
#         return False
    
#     total = sum(weights)
#     for i in range(n):
#         remaining = total - weights[i]
#         if remaining % 2 != 0:
#             continue
#         half = remaining // 2
        
#         curr_sum = 0
#         for j in range(n):
#             if j == i:
#                 continue
#             curr_sum += weights[j]
#             if curr_sum == half:
#                 return True
#     return False
def gold_chain_reconnect(weights):
    n = len(weights)
    if n < 3:
        return False

    total = sum(weights)
    prefix = [0] * (n + 1)
    for k in range(n):
        prefix[k + 1] = prefix[k] + weights[k]

    left_set = set()   # 存 prefix[1..i]，对应"左切"候选
    right_set = {}     # 存 prefix[i+1..n-1] 的频次，对应"右切"候选

    # 初始化 right_set：包含 prefix[1..n-1]
    for k in range(1, n):
        right_set[prefix[k]] = right_set.get(prefix[k], 0) + 1

    for i in range(n):
        # 把 prefix[i+1] 从 right_set 移出（不能用 j=i+1 之前的）
        # 实际上右切范围是 j ∈ [i+1, n-1]，所以先删掉 prefix[i]（对应j=i，已过）
        val = prefix[i + 1]  # 这是 j=i+1 对应的前缀，还在 right_set 里
        # 先从 right_set 里移除 prefix[i]（j=i 这个切点不合法，因为它在 i 左边）
        # 重新理一下：right_set 维护 prefix[i+1 .. n-1]
        # 进入第 i 轮前，需要把 prefix[i+1] ... 算了直接看代码逻辑

        remaining = total - weights[i]
        if remaining % 2 == 0:
            half = remaining // 2
            # 左切：prefix[j] == half，j ∈ [1, i]
            if half in left_set:
                return True
            # 右切：prefix[j] == half + weights[i]，j ∈ [i+1, n-1]
            if (half + weights[i]) in right_set:
                return True

        # 更新 left_set：加入 prefix[i+1]（下一轮 i+1 的左切候选）
        left_set.add(prefix[i + 1])
        # 更新 right_set：移除 prefix[i+1]（下一轮不再是合法右切点）
        if prefix[i + 1] in right_set:
            right_set[prefix[i + 1]] -= 1
            if right_set[prefix[i + 1]] == 0:
                del right_set[prefix[i + 1]]

    return False

print(gold_chain_reconnect([1, 2, 3, 4]))