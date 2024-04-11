# Problem: Nim Game - https://leetcode.com/problems/nim-game/

class Solution:
    def canWinNim(self, n: int) -> bool:
        return bool(n % 4)