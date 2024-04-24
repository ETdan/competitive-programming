# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # outorder=[0]*len(graph)

        indegree = [0] * len(graph)
        answer = []

        adj_list = defaultdict(set)
        q = deque()

        for index, children in enumerate(graph):
            if len(children) == 0:
                q.append(index)
                answer.append(index)
            else:
                indegree[index] = len(children)

            for num in children:
                adj_list[num].add(index)

        while q:
            node = q.popleft()

            for num in adj_list[node]:
                indegree[num]-=1
                if indegree[num] == 0:
                    answer.append(num)
                    q.append(num)

        return sorted(answer)
