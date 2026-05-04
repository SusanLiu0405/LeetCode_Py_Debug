def shared_digits(nums):
    count = [0] * 10
    for num in nums:
        x = num // 10
        y = num % 10
        if x == y:
            count[x] += 1
        else:
            count[x] += 1
            count[y] += 1
    return max(count)

numbers = [52, 25, 11, 52, 34, 55]
print(shared_digits(numbers))