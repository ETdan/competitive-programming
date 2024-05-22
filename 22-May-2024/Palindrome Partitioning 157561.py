# Problem: Palindrome Partitioning - https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        answer=[]
        temp=[]
        
        def dp(curr):
            if curr >= len(s):
                answer.append(temp[:])
            
            for i in range(curr,len(s)):
                if s[curr:i+1] == s[curr:i+1][::-1]:
                    temp.append(s[curr:i+1])
                    dp(i+1)
                    temp.pop()
        
        dp(0)
        return answer