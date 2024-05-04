# Problem: Minimum Height Trees - https://leetcode.com/problems/minimum-height-trees/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        if n == 1:
            return [0]

        adj_list=defaultdict(set)
        q=deque()
        answer=[0]*n

        for node1,node2 in edges:
            adj_list[node1].add(node2)
            adj_list[node2].add(node1)
            
            answer[node1]+=1
            answer[node2]+=1
        

        for i in range(len(answer)):
            if answer[i] == 1:
                q.append(i)

        while q:
            if n <= 2:
                return list(q)

            for i in range(len(q)):
                n-=1
                node = q.popleft()
                for nei in adj_list[node]:
                    answer[nei]-=1
                    if answer[nei] == 1:
                        q.append(nei)