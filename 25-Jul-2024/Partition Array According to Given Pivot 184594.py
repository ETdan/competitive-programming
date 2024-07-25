# Problem: Partition Array According to Given Pivot - https://leetcode.com/problems/partition-array-according-to-given-pivot/description/

class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        lessthan_list=[]
        greaterthan_list=[]
        equal_list=[]
        answer=[]

        for num in nums:
            if num == pivot:
                equal_list.append(num)
            elif num < pivot:
                lessthan_list.append(num)
            else:
                greaterthan_list.append(num)
        return lessthan_list + equal_list + greaterthan_list