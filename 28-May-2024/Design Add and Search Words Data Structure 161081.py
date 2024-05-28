# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(26)]


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            index = ord(c) - ord("a")
            if cur.children[index] == None:
                cur.children[index] = TrieNode()
            cur = cur.children[index]
        cur.is_end = True

    def search(self, word: str) -> bool:
        return self.dp(self.root,word)

    def dp(self,root,word):
        cur = root
        for pos,c in enumerate(word):
            if c == '.':
                for i in range(len(cur.children)):
                    if cur.children[i] and self.dp(cur.children[i],word[pos+1:]):
                        return True
                else:
                    return False
            else:
                index = ord(c) - ord("a")
                if 0 <= index < len(cur.children):
                    if cur.children[index] == None:
                        return False

                    cur = cur.children[index]

        return cur.is_end
    



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
