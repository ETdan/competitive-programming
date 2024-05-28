# Problem: Replace Words - https://leetcode.com/problems/replace-words/

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
    
    def search(self, word,answer):
        cur = self.root
        for c in word:
            index = ord(c) - ord('a')
            if cur.children[index] == None:
                return False
            cur = cur.children[index]
            answer+=c
        
            if cur.is_end:
                return answer
            
        
        return ''

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        tr=Trie()
        sentence=sentence.split()

        for word in dictionary:
            tr.insert(word)
        
        for i in range(len(sentence)):
            answer = tr.search(sentence[i],'')
            if answer:
                sentence[i] = answer
        
        return ' '.join(sentence)