# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        bit=[0]*len(s)
        permu=[]

        @cache
        def dp(i,s):
            if i == len(s):
                permu.append(s)
                # print(s)
                return
            
            if not s[i].isnumeric():
                if s[i].islower():
                    upper = s[:i]+s[i].upper()+s[i+1:]
                    dp(i+1,upper)
                else:
                    lower = s[:i]+s[i].lower()+s[i+1:]
                    dp(i+1,lower)
                dp(i+1,s)
            else:
                dp(i+1,s)

        dp(0,s)
        return permu