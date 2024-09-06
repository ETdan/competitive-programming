# Problem: Pass the Pillow - https://leetcode.com/problems/pass-the-pillow/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        rounds = time // (n - 1)
        return (time % (n - 1) + 1) if rounds % 2 == 0 else (n - time % (n - 1))