def solution(inventory, k):
    n = len(inventory)
    count = 0
    start = 0
    item_count = {} 
    
    for end in range(n):
        item_count[inventory[end]] = item_count.get(inventory[end], 0) + 1

        while len(item_count) >= k:
            count += n - end
            item_count[inventory[start]] -= 1
            if item_count[inventory[start]] == 0:
                del item_count[inventory[start]]
            start += 1
    
    return count