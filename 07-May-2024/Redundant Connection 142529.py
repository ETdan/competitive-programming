# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class Solution:
    parent=[]
    size=[]

    def constract(self,size):
        self.parent=[i for i in range(size)]
        self.size=[1]*size
    
    def union(self,x,y):
        parentx = self.find(x)
        parenty = self.find(y)
        
        if self.size[parentx] > self.size[parenty]:
            self.parent[parenty] = self.parent[parentx]
            self.size[parentx] += self.size[parenty]
        else:
            self.size[parenty] += self.size[parentx]
            self.parent[parentx] = self.parent[parenty]
            

    def find(self,x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x=self.parent[x]
        return x

    def isConnected(self,x,y):
        return self.find(x) == self.find(y)
    
    
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.constract(len(edges))
        # print(self.parent)

        for edge in edges:
            if self.isConnected(edge[0]-1,edge[1]-1):
                return edge
            else:
                self.union(edge[0]-1,edge[1]-1)