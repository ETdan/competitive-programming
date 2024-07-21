# Problem: Merge Intervals (Optional) - https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        i=0
        j=1
        comp=intervals[0][1]
        answer=[]
        while j<len(intervals):
            if comp>=intervals[j][0]:
                comp=max(intervals[j][1],comp)
                j+=1
            else:
                answer.append([intervals[i][0],comp])
                comp=intervals[j][1]
                i=j
                j+=1
        
        
        answer.append([intervals[i][0],comp])
        
        return answer