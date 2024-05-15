# Problem: Longest Common Subsequence - https://leetcode.com/problems/longest-common-subsequence/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}

        def dp(left, right):
            if (left, right) in memo:
                return memo[(left, right)]

            if left == len(text1) or right == len(text2):
                return 0

            if text1[left] == text2[right]:
                memo[(left, right)] = dp(left + 1, right + 1) + 1
            else:
                memo[(left, right)] = max(dp(left + 1, right),dp(left, right + 1))
            
            return memo[(left, right)]
        
        return dp(0,0)