# Problem: Minimize the Maximum of Two Arrays - https://leetcode.com/problems/minimize-the-maximum-of-two-arrays/

class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        f=lambda x:(x+abs(x))//2
        n,prev,d=uniqueCnt1+uniqueCnt2,0,lcm(divisor1,divisor2)
        while n>prev:
            prev=n
            l1,l2=n//divisor2-n//d,n//divisor1-n//d
            n+=f(f(uniqueCnt1-l1)+f(uniqueCnt2-l2)-n+n//d+l2+l1)

        return n    