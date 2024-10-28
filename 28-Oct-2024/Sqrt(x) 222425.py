# Problem: Sqrt(x) - https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
            
        left = 0
        right = x//2
        mid = (left + right)//2

        while left <= right:
            print(mid)
            if mid ** 2 == x:
                return mid 
            elif mid ** 2 < x and (mid + 1) ** 2 > x :
                return mid
            elif mid ** 2 < x:
                left = mid + 1
            else:
                right = mid - 1
            
            mid = (left + right)//2
        