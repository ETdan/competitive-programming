class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        mid = (left + right) // 2

        while left <= right:
            # print(mid, left, right)
            if nums[mid] == target:
                return mid
            elif mid == left == right:
                if nums[mid] > target:
                    return mid 
                else:
                    return mid +1
            elif nums[mid] > target:
                right = mid
            else:
                left = mid + 1

            mid = (left + right) // 2

        return mid - 1 if target > nums[mid] else mid + 1
