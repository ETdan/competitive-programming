class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_=float('-inf')
        left=0
        right=k-1
        sum_=sum(nums[left:right])

        print(nums[left:right])

        while left < len(nums)-k+1:
            sum_ += nums[right]
            
            avg = sum_/k
            max_=max(max_,avg)
        
            sum_ -= nums[left]

            left += 1
            right += 1
            # print(nums[left:right])

        return max_