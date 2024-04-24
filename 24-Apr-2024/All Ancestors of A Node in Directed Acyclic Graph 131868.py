# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj_list = defaultdict(set)
        q = deque()

        indegree = [0] * n
        answer=[set() for _ in range(n)]

        for edge in edges:
            adj_list[edge[0]].add(edge[1])
            indegree[edge[1]] += 1
        
        for index,num in enumerate(indegree):
            if num == 0:
                q.append(index)
        
        while q:
            node = q.popleft()
            
            for num in adj_list[node]:
                indegree[num]-=1
                
                answer[num].add(node)
                answer[num].update(answer[node])
                
                if indegree[num] == 0:
                    q.append(num)

        for index,nums in enumerate(answer):
            answer[index]=sorted(nums)
        
        return answer