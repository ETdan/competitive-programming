# Problem: Sum of Digits of String After Convert - https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        def order(x):
            return str(ord(x)-96)
        num_list=list(map(order,list(s)))
        num_list=''.join(num_list)
        while k:
            k-=1
            num_sum=sum(list(map(int,list(num_list))))
            num_list=list(str(num_sum))

        return int(''.join(num_list))