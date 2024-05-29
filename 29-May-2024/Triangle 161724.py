# Problem: Triangle - https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        cur=triangle[-1]

        for i in range(len(triangle)-2,-1,-1):
            temp = triangle[i]
            for j in range(len(temp)):
                temp[j]+=min(cur[j],cur[j+1])
            cur=temp

        return triangle[0][0]