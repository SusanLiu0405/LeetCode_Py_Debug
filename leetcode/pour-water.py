'''
Water Pouring Problem

You are given two cups with capacities cup1 and cup2. Initially, both cups are empty.

You may perform the following operations in one move:

Empty cup 1
Fill cup 1 to full capacity
Empty cup 2
Fill cup 2 to full capacity
Pour water from cup 1 into cup 2 until either cup 1 is empty or cup 2 is full
Pour water from cup 2 into cup 1 until either cup 2 is empty or cup 1 is full

Return the minimum number of moves required so that either cup contains exactly target units of water. If it is impossible, return -1.
'''
from collections import deque
def pour(cup1: int, cup2: int, target: int) -> int:
    if not cup1 or not cup2 or not target:
        return -1
    if cup1 == target or cup2 == target:
        return 0

    visited = {(0, 0)}
    
    dq = deque()
    dq.append((0, 0))
    pours = 0
    while dq:
        level_size = len(dq)
        for i in range(level_size):
            first_glass, second_glass = dq.popleft()
            next_states = convert(cup1, cup2, first_glass, second_glass, visited)
            for next_state in next_states:
                next_state_first, next_state_second = next_state
                if next_state_first == target or next_state_second == target:
                    return pours + 1
                dq.append(next_state)
                print(next_state_first, next_state_second)
                visited.add(next_state)
        pours += 1
    return -1


def convert(cup1, cup2, first_glass, second_glass, visited):
    result = set()
    # result is a set of tuples, (water_in_first_cup, water_in_second_cup)
    # empty first glass
    next = (0, second_glass)
    if next not in visited:
        result.add(next)
    
    # fill first glass
    next = (cup1, second_glass)
    if next not in visited:
        result.add(next)
    
    # empty second glass
    next = (first_glass, 0)
    if next not in visited:
        result.add(next)
    
    # fill second glass
    next = (first_glass, cup2)
    if next not in visited:
        result.add(next)
    
    # pour water from cup1 to cup2
    second_need = cup2 - second_glass
    if first_glass < second_need:
        next = (0, second_glass + first_glass)
    else:
        next = (first_glass - second_need, cup2)
    if next not in visited:
        result.add(next)
    
    # pour water from cup2 to cup1
    first_need = cup1 - first_glass
    if second_glass < first_need:
        next = (second_glass + first_glass, 0)
    else:
        next = (cup1, second_glass - first_need)
    if next not in visited:
        result.add(next)
    return result

cup1 = 10
cup2 = 1
target = 5
print(pour(cup1, cup2, target))