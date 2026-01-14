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
	# 刚开始的。只存在0或1个星号的
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
	# def can_match(self, s, s_index, parts, p_index, is_end_star):
	#     if p_index == len(parts) and s_index == len(s):
	#         return True
	#
	#     if p_index == len(parts) and is_end_star:
	#         return True
	#
	#     if s_index == len(s):
	#         return False
	#
	#     if p_index == len(parts):
	#         return False
	#
	#
	#     part = parts[p_index]
	#     part_start = s[s_index:].find(part)
	#
	#     while part_start >= 0:
	#         if self.can_match(s, part_start + len(part), parts, p_index + 1, is_end_star):
	#             return True
	#         part_start = s[part_start + len(part):].find(part)
	#
	#     return False

	'''
	这版答案当part abc在找到s中第一次匹配后不可行，还去尝试后面的匹配，这里没必要。
	如果第一次匹配不可信，后面的匹配更不可行
	如果后面的匹配可行，第一次肯定可行
	'''

	# def can_match(self, s, parts, p_index, is_end_star):
	#     if p_index == len(parts):
	#         if not s or is_end_star:
	#             return True
	#         return False
	#
	#     if not s:
	#         return False
	#
	#     part = parts[p_index]
	#     part_start = s.find(part)
	#
	#     while part_start >= 0:
	#         if self.can_match(s[part_start + len(part):], parts, p_index + 1, is_end_star):
	#             return True
	#         s = s[part_start + len(part):]
	#         part_start = s.find(part)
	#
	#     return False

	def can_match(self, s, parts, p_index, is_start_star, is_end_star):
		# p用完了
		if p_index == len(parts):
			# 1. s也完了 2. s没完，但是可以匹配最末尾的*
			if not s or is_end_star:
				return True
			# s没完（最末尾没有*）
			return False

		# p没完了，s完了
		if not s:
			return False

		part = parts[p_index]

		# 不是*开头              最左边的p              必须匹配开头
		if not is_start_star and p_index == 0 and not s.startswith(part):
			return False

		part_start = s.find(part)

		# 如果能找到
		if part_start >= 0:
			return self.can_match(s[part_start + len(part):], parts, p_index + 1, is_start_star, is_end_star)
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
print(s.is_match_multiple_stars('aabbc', 'a*c'))  # False