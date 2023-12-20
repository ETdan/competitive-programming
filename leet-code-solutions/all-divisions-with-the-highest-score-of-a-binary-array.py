class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        answer=[0]
        maxCount=0

        leftCount = 0
        rightCount = nums.count(1)
        onesCount = rightCount

        for  i in range(len(nums)):

            if leftCount + rightCount == maxCount:
                answer.append(i)

            elif leftCount + rightCount > maxCount:
                maxCount = leftCount + rightCount
                answer=[i]

            if nums[i] == 1:
                rightCount -= 1 
            else:
                leftCount += 1
        if len(nums) - onesCount == maxCount:
            answer.append(len(nums))
        if len(nums) - onesCount > maxCount:
            answer=[len(nums)]

        return answer