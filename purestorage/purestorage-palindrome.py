def count_all_palindromic_substrings(s):
    count = 0

    def expand_around_center(left, right):
        nonlocal count
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1

    for i in range(len(s)):
        expand_around_center(i, i)  # 对于奇数长度的回文
        if i + 1 < len(s):
            expand_around_center(i, i + 1)  # 对于偶数长度的回文

    return count

if __name__ == '__main__':
    # test case
    palindrome_count = count_all_palindromic_substrings("wowpurerocks")
    print("Total palindromes:", palindrome_count)
