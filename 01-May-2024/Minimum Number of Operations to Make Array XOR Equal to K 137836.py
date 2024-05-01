# Problem: Minimum Number of Operations to Make Array XOR Equal to K - https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xor=0

        for i in range(len(nums)):
            xor^=nums[i]
        
        return bin(xor^k).count('1')