# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjecency_list = defaultdict(list)
        indegre = [0] * numCourses

        for cource in prerequisites:
            adjecency_list[cource[1]].append(cource[0])
            indegre[cource[0]] += 1

        q = deque()

        for index,node in enumerate(indegre):
            if node == 0:
                q.append(index)

        answer = []

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                answer.append(node)

                for child in adjecency_list[node]:
                    if indegre[child] == 1:
                        q.append(child)
                    indegre[child] -= 1
        

        return answer if len(answer) == numCourses else []
