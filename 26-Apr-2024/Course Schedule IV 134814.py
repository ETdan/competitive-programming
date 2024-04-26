# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

from collections import defaultdict
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        @cache
        def check(n,target):
            nonlocal d
            if n == target:
                return True
            
            for e in d[n]:
                if check(e,target):
                    return True

            return False


        res = []
        d = defaultdict(list)
        for x,y in prerequisites:
            d[x].append(y)
        for x,y in queries:
            res.append(check(x,y))
       
        return res
        # adj_list=defaultdict(set)
        # answer=[]
        # for prerequisite in prerequisites:
        #     adj_list[prerequisite[1]].add(prerequisite[0])

        # for querie in queries:
        #     prereq = querie[0]
        #     course = querie[1]

        #     q= deque()
        #     q.append(course)

        #     found=False
        #     visited=set()

        #     while q:
        #         for _ in range(len(q)):
        #             node = q.popleft()
        #             visited.add(node)

        #             adj_list[prereq].update(adj_list[node])

        #             if course in adj_list[prereq]:
        #                 answer.append(True)
        #                 adj_list[prereq].update(adj_list[course])
        #                 found = True
        #                 break


        #             for children in adj_list[node]:
        #                 adj_list[children].update(adj_list[node])
        #                 if children not in visited:
        #                     q.append(children)
        #                 visited.add(children)
                    
            
        #         if found:
        #             break
            
        #     if not found:
        #         answer.append(False)
        
        # return answer