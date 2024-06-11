# Problem: Minimum Score of a Path Between Two Cities - https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/

class Union:
    def __init__(self, n):
        self.parent = {i:i for i in range(1, n + 1)}

    def find(self,x):
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self,x, y):
        px = self.find(x)
        py = self.find(y)
        self.parent[py] = px

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        union_find = Union(n)
        for u, v, d in roads:
            union_find.union(u, v)
        dist = [d for u, v, d in roads if union_find.find(v) == union_find.find(n)]
        minDist = min(dist)
        return minDist
