# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        i=0
        kc=k
        l=n
        arr=[i for i in range(1,n+1)]

        while l != 1:
            while kc != 0 :
                if i == l:
                    i = 0
                # print(arr[i])
                kc -= 1
                if kc !=0:
                    i += 1

            if i == l:
                i=0
            arr.remove(arr[i])
            # print(arr)
            l -= 1
            kc = k

        for a in arr:
            if a != -1:
                return a
        return 0