def count_all_palindromic_substrings(s):
    all_palindromes = []

    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            all_palindromes.append(s[left:right+1])
            left -= 1
            right += 1

    for i in range(len(s)):
        expand_around_center(i, i)
        if i + 1 < len(s):
            expand_around_center(i, i + 1)

    return len(all_palindromes), all_palindromes

if __name__ == '__main__':
	# test case
	count, palindromes = count_all_palindromic_substrings("www")
	print("Total palindromes:", count)
	print("List palindromes：", palindromes)
