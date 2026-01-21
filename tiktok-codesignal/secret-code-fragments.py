from collections import Counter
# 这个题就是对每个fragment做一个counter
# 对每个counter 寻找可以与之配对的另一个counter item
# if 长得不一样：相乘；if长得一样：n*(n - 1)
def solution(fragments, accessCode):
    s = str(accessCode)
    cnt = Counter(map(str, fragments))
    ans = 0
    for a, count_a in cnt.items():
        if len(a) < len(s) and s.startswith(a):
            b = s[len(a):]
            count_b = cnt.get(b, 0)
            ans += count_a * count_b if a != b else count_a * (count_a - 1)
    return ans

print(solution([777, 7, 777, 77, 77], 7777)) 