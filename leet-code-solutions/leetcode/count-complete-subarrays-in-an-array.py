class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n=len(nums)
        m=len(set(nums))
        ans=0
        for i in range(n):
            sub_set=set()
            for j in range(i,n):
                sub_set.add(nums[j])
                if len(sub_set)==m:
                    ans+=1

        return ans            