# Problem: Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class Solution:
    parent = defaultdict(str)
    size = {}

    def constract(self, s1s2):
        self.parent = {char: char for char in s1s2}
        self.size = {char: 1 for char in s1s2}

    def union(self, x, y):
        parentx = self.find(x)
        parenty = self.find(y)

        if parentx < parenty:
            self.parent[parenty] = self.parent[parentx]
        else:
            self.parent[parentx] = self.parent[parenty]

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        self.constract(s1 + s2)
        answer = []
        for i in range(len(s1)):
            self.union(s1[i], s2[i])

        for char in baseStr:
            x = char
            while x in self.parent and x != self.parent[x]:
                x = self.parent[x]

            answer.append(x)

        return "".join(answer)