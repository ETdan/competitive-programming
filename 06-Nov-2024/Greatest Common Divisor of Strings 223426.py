# Problem: Greatest Common Divisor of Strings - https://leetcode.com/problems/greatest-common-divisor-of-strings/

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len_s1=len(str1)
        len_s2=len(str2)

        i=1
        gcd=""
        answer = ""
        while i <= max(len_s1,len_s2):
            gcd=str1[:i]
            if gcd * (len_s1//i) == str1 and gcd * (len_s2//i) == str2: 
                if len(gcd) > len(answer):
                    answer = gcd

            i+=1 
        return answer