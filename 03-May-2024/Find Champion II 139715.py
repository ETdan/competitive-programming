# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indegree={i for i in range(n)}

        for u,v in edges:
            if v in indegree:
                indegree.remove(v)
        
        if len(indegree)==1:
            return indegree.pop()
        else:
            return -1