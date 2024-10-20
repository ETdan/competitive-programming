# Problem: Kth Smallest Element in a Sorted Matrix - https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        answer=[]
        for i in range(len(matrix)):
            answer.extend(matrix[i])
        answer.sort()
        return answer[k-1]