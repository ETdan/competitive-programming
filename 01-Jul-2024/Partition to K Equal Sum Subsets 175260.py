# Problem: Partition to K Equal Sum Subsets - https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

        if sum(nums)%k!=0:
            return False
        
        nums.sort(reverse=True)
        target = sum(nums)/k
        used=[False]*len(nums)

        def backtrack(i,k,curSum):
            if k==0:
                return True
            
            if curSum==target:
                return backtrack(0,k-1,0)
            
            for j in range(i,len(nums)):
                if used[j] or curSum + nums[j] > target:
                    continue
                used[j]=True
                if backtrack(j+1,k,curSum+nums[j]):
                    return True
                used[j]=False
            
                if curSum == 0:
                    return False
                
            return False
            
        return backtrack(0,k,0)