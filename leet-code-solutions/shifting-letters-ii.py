class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        pre=[0]*(len(s)+1)
        alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        answer=[]

        for l,r,d in shifts:
            if d == 0:
                pre[l]+=-1
                pre[r+1]+=1
            else:
                pre[l]+=1
                pre[r+1]+=-1

        for i in range(1,len(pre)):
            pre[i]+= pre[i-1]
        
        for i in range(len(s)):
            answer.append(alpha[(alpha.index(s[i]) + pre[i])%26])
        
        return "".join(answer)