# Problem: Longest Arithmetic Subsequence of Given Difference - https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/description/

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        Dict = {}
        for num in arr:
            if num - difference in Dict:
                Dict[num] = Dict[num - difference] + 1
            else:
                Dict[num] = 0
                
        max_=0
        for key,val in Dict.items():
            max_=max(max_,val)
        
        return max_ + 1