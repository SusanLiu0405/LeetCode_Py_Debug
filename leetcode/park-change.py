'''
start: "AB$C"
target: "ACB$"
$ 可以和任意位置的char交换
Parking Slot Swap

You are given two strings, start and target, of the same length.
Each string contains the same set of characters and exactly one special empty slot represented by '$'.

In one move, you may swap '$' with any other character in the string.

Return the minimum number of moves required to transform start into target. If it is impossible, return -1.
'''
from collections import deque
def parkChange(start: str, target: str) -> int:
    if start == target:
        return 0
    if not start or not target:
        return -1
    visited = {}
    visited[start] = True
    moves = 0
    dq = deque()
    dq.append(start)
    while dq:
        level_size = len(dq)
        for i in range(level_size):
            currState = dq.popleft()
            nextStates = convert(currState, visited)
            print(nextStates)
            for next in nextStates:
                if next == target:
                    return moves + 1
                dq.append(next)
                visited[next] = True
        moves += 1
    return -1

def convert(curr, visited):
    nexts = set()
    currChar = list(curr)
    dollar_idx = currChar.index('$')
    for idx in range(len(currChar)):
        if currChar[idx] == '$':
            continue
        currChar[idx], currChar[dollar_idx] = currChar[dollar_idx], currChar[idx]
        newChar = "".join(currChar)
        if newChar not in visited:
            nexts.add(newChar)
        currChar[idx], currChar[dollar_idx] = currChar[dollar_idx], currChar[idx]
    return nexts

start = "ABC$"
target = "$ABC"
print(parkChange(start, target))

'''
对start：里面有n个字母，因此整个start有n!个状态；convert的时候时间复杂度是n^2
所以时间复杂度是n!*n^2 


'''