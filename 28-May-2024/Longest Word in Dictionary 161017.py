# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class TrieNode:
    def __init__(self):
        self.is_end=False
        self.children=[None for _ in range(26)]

class Trie:
    def __init__(self):
        self.root=TrieNode()
    
    def insert(self,word):
        curr=self.root

        for c in word:
            index = ord(c)-ord('a')

            if curr.children[index] == None:
                curr.children[index] = TrieNode()
            
            curr=curr.children[index]

        curr.is_end=True

class Solution:

    def longestWord(self, words: List[str]) -> str:
        tr = Trie()
        for i in range(len(words)):
            tr.insert(words[i])
        answer=''

        def dfs(root,word):
            nonlocal answer
            for index in range(len(root.children)):
                if root.children[index] != None and root.children[index].is_end :
                    # print(chr(ord('a')+index))
                    dfs(root.children[index],word+chr(ord('a')+index))
            # print("////////////",word)

            if len(answer)< len(word):
                answer=word

        dfs(tr.root,'')
        return answer