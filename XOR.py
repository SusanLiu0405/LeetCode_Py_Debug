n = int(input())
arr = list(map(int, input().split()))


class Node:
	def __init__(self):
		self.zero = None
		self.one = None
		self.cnt = 0


trie_root = Node()

def insert(num):
	curr = trie_root

	for i in range(20, -1, -1):
		if (1 << i) & num:
			if curr.one == None:
				curr.one = Node()
			curr = curr.one
			curr.cnt += 1
		else:
			if curr.zero == None:
				curr.zero = Node()
			curr = curr.zero
			curr.cnt += 1


insert(arr[0])

ans = 0

for i in range(1, len(arr)):
	curr = trie_root
	for j in range(20, -1, -1):
		if (1 << j) & arr[i] == 0:
			if curr.zero == None:
				break
			else:
				curr = curr.zero
		else:
			if curr.one != None:
				ans += curr.one.cnt
			break
	insert(arr[i])

print(ans)

