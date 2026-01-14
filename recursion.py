def sum(total, count):
    while count == 0:
        return total
    return sum(total + count, count - 1)

total = 0
count = 100
print(sum(total, count))
