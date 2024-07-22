# Problem: Number of Pairs Satisfying Inequality - https://leetcode.com/problems/number-of-pairs-satisfying-inequality/

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:

        new_arr=[]

        for i in range(len(nums1)):
            new_arr.append(nums1[i]-nums2[i])

        answer = 0

        def mearger(left_half, right_half):
            left = right = 0
            answer = []

            while left < len(left_half) and right < len(right_half):
                if left_half[left] <= right_half[right]:
                    answer.append(left_half[left])
                    left += 1
                else:
                    answer.append(right_half[right])
                    right += 1

            answer.extend(left_half[left:])
            answer.extend(right_half[right:])

            return answer

        def mergeSort(left, right, nums):
            nonlocal answer

            if left == right:
                return [nums[left]]

            mid = left + (right - left) // 2

            left_half = mergeSort(left, mid, nums)
            right_half = mergeSort(mid + 1, right, nums)

            i = j = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] <= right_half[j] + diff:
                    i += 1
                    answer += len(right_half) - j
                else:
                    j += 1
            
            # print(i,j)

            return mearger(left_half, right_half)

        mergeSort(0, len(new_arr) - 1, new_arr)

        return answer
