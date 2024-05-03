# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indegree=[0]*n

        for u,v in edges:
            indegree[v]+=1
        
        zeroCounter=0
        champion=-1
        
        for index,num in enumerate(indegree):
            if num ==0:
                zeroCounter+=1
                champion=index
                if zeroCounter > 1:
                    return -1
        
        if zeroCounter==1:
            return champion