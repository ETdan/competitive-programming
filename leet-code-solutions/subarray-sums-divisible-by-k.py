class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainder_counter = {0:1}
        currSum=0
        answer=0

        for i in range(len(nums)):
            currSum+=nums[i]

            if currSum % k in remainder_counter:
                answer += remainder_counter[currSum%k]
            remainder_counter[currSum%k] = 1 + remainder_counter.get(currSum%k,0)
        
        return answer