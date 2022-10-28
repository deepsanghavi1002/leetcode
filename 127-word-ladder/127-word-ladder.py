class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        combDict = defaultdict(list)
        L = len(beginWord)
        for word in wordList:
            for i in range(L):
                combDict[word[:i]+"*"+word[i+1:]].append(word)
        print(combDict)
        q = collections.deque([(beginWord,1)])
        visited = {beginWord: True}
        while q:
            currentWord, level = q.popleft()
            for i in range(L):
                intermediate_word = currentWord[:i] + "*" + currentWord[i+1:]
                for word in combDict[intermediate_word]:
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        visited[word] = True
                        q.append((word, level+1))
                combDict[intermediate_word] = []
        return 0