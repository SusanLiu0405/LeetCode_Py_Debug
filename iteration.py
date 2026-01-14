def sum(total, count):
    while count > 0:
        total += count
        count -= 1
    return total
total = 0
count = 100
print(sum(total, count))