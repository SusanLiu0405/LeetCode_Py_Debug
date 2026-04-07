from collections import deque
from collections import defaultdict
from typing import List
def ladderLength(beginWord: str, endWord: str, wordList: List[str]):
    charToWord = {}
    dq = deque()
    dq.append(beginWord)

    for word in wordList:
        ch = word[0]
        if ch not in charToWord:
            charToWord[ch] = set()
        charToWord[ch].add(word)

    charToWord[beginWord[0]].discard(beginWord)
    print("charToWord", charToWord)

    level = 1
    while dq:
        size = len(dq)
        for _ in range(size):
            currWord = dq.popleft()
            ch = currWord[-1]
            nextSet = charToWord.get(ch)
            if nextSet is None:
                continue
            for nextWord in nextSet:
                if nextWord == endWord:
                    return level + 1
                dq.append(nextWord)
            del charToWord[ch]
        level += 1
    return 0
            

wordList = ["hot", "tag", "gov", "vic", "cam"]
wordSet = set(wordList)
beginWord = "hot"
endWord = "cam"

print(ladderLength(beginWord, endWord, wordList))


'''

'''