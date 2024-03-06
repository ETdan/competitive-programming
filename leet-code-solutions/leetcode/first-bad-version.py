# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        min_bad = float("inf")
        left = 0
        right = n
        mid = (right + left) // 2
        
        while left <= right:
            if isBadVersion(mid):
                min_bad = min(min_bad,mid)
                right= mid - 1
            else:
                left = mid  + 1
            mid = (right + left) // 2
        
        return min_bad
        