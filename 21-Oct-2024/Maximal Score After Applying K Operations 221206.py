# Problem: Maximal Score After Applying K Operations - https://leetcode.com/problems/maximal-score-after-applying-k-operations

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = -1 * nums[i]
        
        heapq.heapify(nums)
        score=0

        for i in range(k):
            cur_score=heapq.heappop(nums)
            heapq.heappush(nums,-ceil((-cur_score)/3))
            score+=cur_score

        return -score