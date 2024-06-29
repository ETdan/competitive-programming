# Problem: Short Encoding of Words - https://leetcode.com/problems/short-encoding-of-words/

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(26)]


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root

        for c in word:
            index = ord(c) - ord("a")

            if curr.children[index] == None:
                curr.children[index] = TrieNode()

            curr = curr.children[index]
            curr.is_end = False

        curr.is_end = True


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        root = Trie()

        words.sort(key=lambda word: len(word))
        for word in words:
            root.insert(word[::-1])

        answer = 0

        def dfs(cur, count):
            nonlocal answer

            for node in cur.children:
                if node != None:
                    dfs(node, count + 1)

            if cur.is_end == True:
                answer += count + 1

        dfs(root.root, 0)

        return answer
