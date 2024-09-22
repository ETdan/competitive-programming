# Problem: B - Gelada baboon's Family Trees - https://codeforces.com/gym/520688/problem/B

import sys

input = sys.stdin.readline


class UnionFind:
    parent = []
    size = []

    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.size = [1] * size

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        parentx = self.find(x)
        parenty = self.find(y)

        if self.size[parentx] > self.size[parenty]:
            self.parent[parenty] = self.parent[parentx]
            self.size[parentx] += self.size[parenty]
        else:
            self.size[parenty] += self.size[parentx]
            self.parent[parentx] = self.parent[parenty]


t = int(input())
arr = list(map(int, input().split()))

for index in range(len(arr)):
    arr[index] -= 1

un = UnionFind(len(arr))

for index in range(len(arr)):
    un.union(index, arr[index])

counter = 0
for i in range(len(un.parent)):
    if i == un.parent[i]:
        counter += 1

print(counter)
