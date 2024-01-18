class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        answer=0
        sum_=0
        counter=defaultdict(int)
        counter[0]=1        
        for i in range(len(nums)):
            sum_ += nums[i]
            if sum_ - k in counter:
                answer += counter[sum_ - k]
            counter[sum_]+=1
        
        return answer
