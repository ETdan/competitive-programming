# Problem: XOR Queries of a Subarray - https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        for i in range(len(arr)):
            if i>0:
                arr[i]=arr[i]^arr[i-1]
        answer=[]
        
        for l,r in queries:
            xor=arr[r]
            if l>0:
                xor^=arr[l-1]
            answer.append(xor)

        return answer
        