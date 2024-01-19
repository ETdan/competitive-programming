class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        answer=0
        sum_=0
        counter=defaultdict(int)
        counter[0]=1        
        for i in range(len(nums)):
            sum_ += nums[i]
            if sum_ - goal in counter:
                answer += counter[sum_ - goal]
            counter[sum_]+=1
        
        return answer