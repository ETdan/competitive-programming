# Problem: Smallest String With Swaps - https://leetcode.com/problems/smallest-string-with-swaps/

class Solution:
    parent = []
    size = []

    def constract(self, size):
        self.parent = [i for i in range(size)]
        self.size = [1] * size

    def union(self, x, y):
        # print(x,y)
        parentx = self.find(x)
        parenty = self.find(y)

        if parentx != parenty:
            if self.size[parentx] > self.size[parenty]:
                self.parent[parenty] = self.parent[parentx]
                self.size[parentx] += self.size[parenty]
            else:
                self.size[parenty] += self.size[parentx]
                self.parent[parentx] = self.parent[parenty]

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        self.constract(len(s))
        for i,j in pairs:
            self.union(i,j)
        
        group = defaultdict(lambda: ([], []))  
        for i, ch in enumerate(s):
            parent = self.find(i)
            group[parent][0].append(i)
            group[parent][1].append(ch)

        res = [''] * len(s)
        for ids, chars in group.values():
            ids.sort()
            chars.sort()
            for ch, i in zip(chars, ids):
                res[i] = ch
                
        return ''.join(res)