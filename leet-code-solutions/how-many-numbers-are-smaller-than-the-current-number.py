class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortedNums=sorted(nums)
        answer=[]
        for num in nums:
            answer.append(sortedNums.index(num))
        return answer