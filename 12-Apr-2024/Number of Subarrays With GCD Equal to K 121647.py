# Problem: Number of Subarrays With GCD Equal to K - https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/description/

class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        answer = 0
        gcd = k
        
        for i in range(len(nums)):
            gcd = nums[i]

            for j in range(i , len(nums)):
                gcd = math.gcd(gcd, nums[j])
                if gcd == k:
                    answer += 1
                elif gcd < k:
                    break
        
        return answer