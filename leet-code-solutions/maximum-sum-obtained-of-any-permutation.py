class Solution:
    mod = pow(10,9) + 7
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n=len(nums)
        pre_sum=[0]*n
        for start,end in requests:
            pre_sum[start]+=1
            if end<n-1:
                pre_sum[end+1]-=1

        for i in range(1,n):
            pre_sum[i]+=pre_sum[i-1]
        
        pre_sum.sort()
        nums.sort()
        sum_=0
        for i in range(n):
            sum_ += nums[i] * pre_sum[i] 

        return sum_ % self.mod
