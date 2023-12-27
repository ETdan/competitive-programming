class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        answer=[]
        for x,y in points:
            answer.append(x)
        answer.sort()

        maxVa=0
        
        for i in range(len(answer)-1):
            if maxVa < answer[i+1] - answer[i]:
                maxVa=answer[i+1] - answer[i]
        
        return maxVa
