class Solution:
    def maxScore(self, s: str) -> int:
        sum_,max_=0,0
        for i in range(1,len(s)):
            if s[i] == "1":
                sum_+=1
        temp= s[0]=="0"
        max_=max(max_,sum_+temp)
        for i in range(1,len(s)-1):
            if s[i] == "0":
                temp+=1

            max_=max(max_,sum_+temp)
            if s[i] == "1":
                sum_ -= 1

        
        return max_
