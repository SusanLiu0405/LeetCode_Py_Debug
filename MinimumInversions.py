def get_minimum_inversions(ls):
    max_num = max(ls)
    range_end_num = get_range_end_num(max_num)
    least_cnt = float('inf')
    result = 0
    for num in range(1, range_end_num + 1):
        curr_cnt = get_inversions_cnt(ls, num)
        if curr_cnt < least_cnt:
            least_cnt = curr_cnt
            result = num
    return result

def get_range_end_num(max_num):
    end_num = 1
    while max_num > end_num - 1:
        end_num *= 2

    return end_num - 1

def get_inversions_cnt(ls, num):
    ls_after_xor = []
    for n in ls:
        ls_after_xor.append(n ^ num)
    return cnt_inversions(ls_after_xor)

def cnt_inversions(ls):
    cnt = 0
    for i in range(len(ls)):
        for j in range(i + 1, len(ls)):
            if ls[i] > ls[j]:
                cnt += 1
    return cnt

# https://codeforces.com/contest/1417/problem/E 原题的测试用例和这个链接的用例全通过了
print(get_minimum_inversions([8, 5, 2])) # 12
print(get_minimum_inversions([0, 1, 3, 2])) # 1
print(get_minimum_inversions([10, 7, 9, 10, 7, 5, 5, 3, 5])) # 14
print(get_minimum_inversions([8, 10, 3])) # 8