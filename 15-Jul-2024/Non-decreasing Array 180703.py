# Problem: Non-decreasing Array - https://leetcode.com/problems/non-decreasing-array/

class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def isSorted(number):
            return number == sorted(number)

        modify=False

        sorted_nums=sorted(nums)

        for i in range(len(nums)-1):
            if nums[i] > nums[i+1] and not modify:
                
                if isSorted(nums[:i]+[nums[i+1]]+nums[i+1:]):
                    print("first")
                    modify=True
                elif isSorted(nums[:i+1]+[nums[i]]+nums[i+2:]):
                    print("second")
                    modify=True
                else:
                    # print(nums[:i+1]+[nums[i]]+nums[i+2:])
                    # print(nums[:i]+[nums[i+1]]+nums[i+1:])
                    # print(sorted_nums)

                    return False
            
        return True
        