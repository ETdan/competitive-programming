# Problem: Longest Increasing Path in a Matrix - https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

class Solution2:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows,cols=len(matrix),len(matrix[0])
        dp={}
        def dfs(r,c,prevVal):
            if r < 0 or r == rows or c < 0 or c == cols or matrix[r][c] <= prevVal:
                return 0
            if (r,c) in dp:
                return dp[(r,c)]
            res=1   # an individual element is also an inc path
            res=max(res,1+dfs(r+1,c,matrix[r][c]),1+dfs(r-1,c,matrix[r][c]),1+dfs(r,c-1,matrix[r][c]),1+dfs(r,c+1,matrix[r][c]))

            dp[(r,c)] = res
            return dp[(r,c)] 
        
        for r in range(rows):
            for c in range(cols):
                dfs(r,c,-1) # -1 bcz we don't want to  matrix[r][c] <= prevVal true initially
        return max(dp.values())

# time/space complexity -> O(n.m)


# TOPOLOGICAL SORT

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows=len(matrix)
        cols=len(matrix[0])
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        # Calculate indegree
        indegree=[[0]*cols for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                for nr, nc in directions:
                    currR=r+nr
                    currC=c+nc
                    if (0<=currR<rows and           # valid conditions
                        0<=currC<cols and
                        matrix[r][c]<matrix[currR][currC]):
                        indegree[currR][currC]+=1
        q=deque()
        for r in range(rows):
            for c in range(cols):
                if indegree[r][c]==0:
                    # row, column, total cells in path
                    q.append((r,c,1))
        path=0
        # Traverse using topological sort (Kahn's algorithm)
        while q:
            r,c,path=q.popleft()
            for nr, nc in directions:
                currR=r+nr
                currC=c+nc
                if (0<=currR<rows and
                    0<=currC<cols and
                    matrix[r][c]<matrix[currR][currC]):       # shows increasing order

                    indegree[currR][currC]-=1
                    if indegree[currR][currC]==0:
                        q.append((currR,currC,path+1))

        return path