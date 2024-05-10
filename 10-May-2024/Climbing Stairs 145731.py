# Problem: Climbing Stairs - https://leetcode.com/problems/climbing-stairs/

class Solution:
    memo=defaultdict(int)
    def climbStairs(self, n: int) -> int:
        if n < 4:
            return n
        if n not in self.memo:
            self.memo[n]=self.climbStairs(n-1) + self.climbStairs(n-2)
        
        return self.memo[n]
