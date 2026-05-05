def lengthOfLIS(nums) -> int:
        if not nums:
            return 0
        tail = []
        for num in nums:
            index = getIndex(tail, num)
            print("num = ", num, "index =", index)
            if index == len(tail):
                tail.append(num)
            else:
                tail[index] = num
        return len(tail)

def getIndex(tail, num):
    left = 0
    right = len(tail) - 1
    while left <= right:
        mid = (left + right) // 2
        if tail[mid] == num:
            return mid
        elif tail[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
    return left

nums = [10,9,2,5,3,7,101,18]
print(lengthOfLIS(nums))