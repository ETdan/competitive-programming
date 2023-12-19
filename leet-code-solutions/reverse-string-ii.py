class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        answer=""
        left=0
        right=min(k,len(s))

        while left < (len(s)):
            # firstPart=s[i:i+k][::-1]
            # i+=k
            # secondPart=s[i:i+k]
            # i+=k
            # answer+=firstPart
            # answer+=secondPart
            answer+=s[left:left+k][::-1]
            left+=k
            answer+=s[left:left+k]
            left+=k
            right=min(left+k,len(s))
        
        return answer
            
