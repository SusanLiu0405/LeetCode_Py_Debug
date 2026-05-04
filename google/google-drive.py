def findMinIncrease(tree_nodes, tree_from, tree_to, access_level):
    graph = [[] for _ in range(tree_nodes + 1)]
    for u, v in zip(tree_from, tree_to):
        graph[u].append(v)
        graph[v].append(u)
    curr_level = list(access_level)

    def post_order(curr, parent):
        for neighbor in graph[curr]:
            if neighbor != parent:
                post_order(neighbor, curr)
                curr_level[curr - 1] = max(curr_level[curr - 1], curr_level[neighbor - 1] - 1)
    
    def pre_order(curr, parent):
        for neighbor in graph[curr]:
            if neighbor != parent:
                curr_level[neighbor - 1] = max(curr_level[neighbor - 1], curr_level[curr - 1] - 1)
                pre_order(neighbor, curr)
    
    post_order(1, -1)
    pre_order(1, -1)
    total_diff = 0
    for i in range(tree_nodes):
        total_diff += curr_level[i] - access_level[i]
    return total_diff
    

tree_nodes = 5
tree_from = [1, 2, 2, 3]
tree_to = [2, 3, 4, 5]
curr = 3
neighbor = [2, 5]
access_level = [1, 4, 2, 6, 5]
graph = [[], [2], [1, 3, 4], [2, 5], [2], [3]]

print(findMinIncrease(tree_nodes, tree_from, tree_to, access_level))

'''
    1(3)
    |
    2(4)
   /    \
  3(5)  4(6)
  \
    5(5)
'''

'''
    1(1)
    |
    2(4)
   /    \
  3(2)  4(6)
  \
    5(5)
'''