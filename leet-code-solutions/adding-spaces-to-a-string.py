class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        left=0
        answer=[]
        spaces = set(spaces)
        for i in range(len(s)):
            if i in spaces:
                answer.append(" ")
                answer.append(s[i])            
                # index=spaces.index(i+1)
                # if index+1 < len(spaces):
                #     spaces[index+1]+=1
            else:           
                answer.append(s[i])            
            
        return "".join(answer)
        