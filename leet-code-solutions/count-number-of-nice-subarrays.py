class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        k_counter, k_minus_1_counter = 0, 0

        counter, left = 0, 0
        for right in range(len(nums)):
            if nums[right] % 2 != 0:
                counter += 1
            while counter > k and left < len(nums):
                if nums[left] % 2 != 0:
                    counter -= 1
                left += 1

            k_counter += right - left + 1
            # print(left, right, k_counter)

        counter, left = 0, 0
        for right in range(len(nums)):
            if nums[right] % 2 != 0:
                counter += 1
            while counter > k - 1 and left < len(nums):
                if nums[left] % 2 != 0:
                    counter -= 1
                left += 1

            k_minus_1_counter += right - left + 1
            # print(left, right, k_minus_1_counter)

        return k_counter - k_minus_1_counter
