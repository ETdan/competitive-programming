# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        answer=[[i,quiet[i]] for i in range(len(quiet))]
        adj_list=defaultdict(set)

        inorder =[0] * len(quiet) 
        
        for edge in richer:
            adj_list[edge[0]].add(edge[1])
            inorder[edge[1]]+=1

        q=deque()
        
        # print(adj_list)
        # print(inorder)
        
        for index,num in enumerate(inorder):
            if num == 0:
                q.append(index)

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                for children in adj_list[node]:
                    # print("bbb",children,node,answer[children] ,answer[node])
                    if answer[children][1] > answer[node][1]:
                        # print(children,node,answer[children] ,answer[node])
                        answer[children] = answer[node]
                    
                    inorder[children]-=1
                    if inorder[children] == 0:
                        q.append(children)
                        
        # print(answer)
        # print(inorder)

        return [x for x,y in answer]
