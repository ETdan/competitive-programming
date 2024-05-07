# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/

class Solution:
    parent = []
    size = []

    def constract(self, size):
        self.parent = [i for i in range(size)]
        self.size = [1] * size

    def union(self, x, y):
        parentx = self.find(x)
        parenty = self.find(y)

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

    def isConnected(self, x, y):
        return self.find(x) == self.find(y)

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                d1 = abs(points[j][0] - points[i][0])
                d2 = abs(points[j][1] - points[i][1])
                edges.append([i, j, d1 + d2])
        edges.sort(key=lambda x: x[2])

        
        self.constract(len(points))

        weight = 0

        for edge in edges:
            if not self.isConnected(edge[0], edge[1]):
                self.union(edge[0], edge[1])
                weight += edge[2]

        return weight
