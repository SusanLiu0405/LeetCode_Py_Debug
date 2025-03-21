def findLoser(videoSequence, k):
    stack = []
    moves = 0  # how many pairs have been removed

    # Iterate from the last character to the first
    for c in reversed(videoSequence):
        if stack and stack[-1] == c:
            # Found a matching pair with the top of the stack, pop and count a move
            stack.pop()
            moves += 1
        else:
            # Otherwise, push current character
            stack.append(c)
        print(stack)

    loser = (moves % k) + 1
    return loser


# --- Example Usage ---
# For the sample "baabzzpq" with k=4, let's verify your scenario:

if __name__ == "__main__":
	s = "xyzabc"
	k = 2
	result = findLoser(s, k)
	print(result)