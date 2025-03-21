def get_min_product_sum(ls):
    size = len(ls)
    cnt = 0
    results = [0] * size
    while cnt < size:
        remainder = cnt % 4
        if remainder == 0:
            results[(cnt // 4) * 2] = ls[size - 1 - (cnt // 4) * 2]
        elif remainder == 1:
            results[size - 1 - (cnt // 4) * 2]  = ls[size - 2 - (cnt // 4) * 2]
        elif remainder == 2:
            results[(cnt // 4) * 2 + 1]= ls[(cnt // 4) * 2]
        # remainder == 3
        else:
            results[size - 2 - (cnt // 4) * 2] = ls[(cnt // 4) * 2 + 1]
        cnt += 1
    return results


print(get_min_product_sum([1,2,6,6,7,10,10])) # [10, 1, 7, 6, 6, 2, 10]
print(get_min_product_sum([1,2,3,4,5,6,7])) # [7, 1, 5, 3, 4, 2, 6]
print(get_min_product_sum([1,2,3])) # [3, 1, 2]
print(get_min_product_sum([100, 1, 2, 3]))
print(get_min_product_sum([1]))
print(get_min_product_sum([1, 1, 1]))

