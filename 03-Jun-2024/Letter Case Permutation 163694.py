# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        bit=[0]*len(s)
        answer=[]

        def recur(i,s):
            if i == len(s):
                answer.append(s)
                return
            
            if not s[i].isnumeric():
                if s[i].islower():
                    upper = s[:i]+s[i].upper()+s[i+1:]
                    recur(i+1,upper)
                else:
                    lower = s[:i]+s[i].lower()+s[i+1:]
                    recur(i+1,lower)
                recur(i+1,s)
            else:
                recur(i+1,s)

        recur(0,s)
        return answer