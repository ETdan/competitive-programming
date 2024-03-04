class Solution:
    def splitString(self, s: str) -> bool:
        answer=[]
        def backTrack(start):
            if start == len(s):
                return len(answer) > 1 
            
            for i in range(start,len(s)):
                m = int(s[start:i+1])
                if answer and answer[-1] - m != 1:
                    continue
                
                answer.append(m)
                if backTrack(i+1):
                    return True
                answer.pop()

        return backTrack(0)