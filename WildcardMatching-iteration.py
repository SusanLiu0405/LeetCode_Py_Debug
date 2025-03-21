'''
题目是这道题只有星号的情况
刚开始只需要写只有零或一个*
写完零或一个*后
要写非dp版本的多个星号的情况
两种情况都需要自己跑一下给的测试案例确保正确
解答：不能用dp，用官方答案里面的解法就好了。

* = 0 or N characters

https://leetcode.com/problems/wildcard-matching/
'''
class Solution:
    # 0 or 1 *
    def is_match(self, s, p):
        if '*' not in p:
            return s == p

        parts = p.split('*')
        # s = ab ccccc cd
        # p = ab *     cd

        # s = acd
        # p = ac *     cd
        return s.startswith(parts[0]) and s[len(parts[0]):].endswith(parts[1])

    # could two consecutive stars exists? a**b
    def is_match_multiple_stars(self, s, p):
        parts = p.split('*')
        # filter out empty parts
        parts = [part for part in parts if part]
        is_start_star = p[0] == '*'
        is_end_star = p[-1] == '*'

        # if not is_start_star:
        #     if s.find(parts[0]) == -1: # 比较开头是否相等
        #         return False
        #     return self.can_match(s[len(parts[0]):], parts, 1, is_end_star)

        return self.can_match(s, parts, 0, is_start_star, is_end_star)

    '''
    abc xyz lmn
    abc *
    
    abc xyz lmn uvw
    abc *   lmn
    
    abc xyz lmn uvw
    abc *   lmn
    '''

    def is_match_multiple_stars_iterate(self, s, p):
        parts = p.split('*')
        # filter out empty parts
        parts = [part for part in parts if part]
        is_start_star = p[0] == '*'
        is_end_star = p[-1] == '*'

        p_index = 0

        if not is_start_star and p_index == 0 and not s.startswith(parts[p_index]):
            return False

        # p和s都没完
        while p_index < len(parts) and s:
            part = parts[p_index]
            # 比如abcabc里面找abc。如果前面的部分，都找不到abc，那更不用考虑在后面接着找abc了
            part_start = s.find(part)
            if part_start == -1:
                return False
            # match完了。把这段切了
            s = s[part_start + len(part):]
            p_index += 1

        # p完了
        if p_index == len(parts):
            # 1. s也完了 2. s没完，但是可以匹配最末尾的*
            if not s or is_end_star:
                return True
            # s没完（最末尾没有*）
            return False

        # p没完了，s完了。能到这行肯定p没完。
        return False




s = Solution()
# print(s.is_match('abcd', 'abcd')) # True
# print(s.is_match('abcd', 'a*d')) # True
# print(s.is_match('acd', 'ac*cd')) # False

# s and p
# print(s.is_match_multiple_stars('abcd', 'abcd')) # True
# print(s.is_match_multiple_stars('abcd', 'a*d')) # True
# print(s.is_match_multiple_stars('abcde', 'a*c*e')) # True
# print(s.is_match_multiple_stars('abcde', 'a*c*')) # True
# print(s.is_match_multiple_stars('abcde', 'a*c')) # False
# print(s.is_match_multiple_stars('abcbde', 'a*b*bde')) # True
# print(s.is_match_multiple_stars('abcbde', 'a*b*bde')) # True, b in a*b*bde must match first b
# print(s.is_match_multiple_stars('aab', '*ab')) # True
# print(s.is_match_multiple_stars('aab', 'ab')) # False
# print(s.is_match_multiple_stars('aab', 'aa')) # False
# print(s.is_match_multiple_stars('aab', 'aa*')) # True
# print(s.is_match_multiple_stars('aba', 'a*a*c')) # False


print(s.is_match_multiple_stars_iterate('abcd', 'abcd')) # True
print(s.is_match_multiple_stars_iterate('abcd', 'a*d')) # True
print(s.is_match_multiple_stars_iterate('abcde', 'a*c*e')) # True
print(s.is_match_multiple_stars_iterate('abcde', 'a*c*')) # True
print(s.is_match_multiple_stars_iterate('abcde', 'a*c')) # False
print(s.is_match_multiple_stars_iterate('abcbde', 'a*b*bde')) # True
print(s.is_match_multiple_stars_iterate('abcbde', 'a*b*bde')) # True, b in a*b*bde must match first b
print(s.is_match_multiple_stars_iterate('aab', '*ab')) # True
print(s.is_match_multiple_stars_iterate('aab', 'ab')) # False
print(s.is_match_multiple_stars_iterate('aab', 'aa')) # False
print(s.is_match_multiple_stars_iterate('aab', 'aa*')) # True
print(s.is_match_multiple_stars_iterate('aba', 'a*a*c')) # False
