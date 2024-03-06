class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        answer = []

        # find left most occurrence
        left = 0
        right = len(nums) - 1
        l=-1
        mid = (left + right)//2
        while left <= right:
            if nums[mid] == target:
                l=mid
                right =mid - 1 
            elif nums[mid] > target:
                right =mid - 1 
            else:
                left = mid+1
            
            mid = (left + right)//2
        
        answer.append(l)


        # find right most occurrence
        left = 0
        right = len(nums) - 1
        r=-1
        mid = (left + right)//2

        while left <= right:
            if nums[mid] == target:
                r=mid
                left = mid+1
            elif nums[mid] > target:
                right =mid - 1 
            else:
                left = mid+1
            
            mid = (left + right)//2
        
        answer.append(r)

        return answer