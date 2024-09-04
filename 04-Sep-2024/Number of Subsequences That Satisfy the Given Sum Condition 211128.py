# Problem: Number of Subsequences That Satisfy the Given Sum Condition - https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        answer=0
        j=len(nums)-1

        mod=(10**9+7)

        for i in range(len(nums)):
            while i<=j and nums[i]+nums[j]>target:
                j-=1

            if i <= j:
                answer+=2**(j-i)
                answer%=mod
        
        return answer