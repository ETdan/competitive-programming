# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

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
        while x!= self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x=self.parent[x]
        return x

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.constract(len(isConnected))

        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j]==1:
                    self.union(i,j)
        
        provinces=0

        for num in range(len(self.parent)):
            if self.parent[num] == num:
                provinces+=1

        
        return provinces