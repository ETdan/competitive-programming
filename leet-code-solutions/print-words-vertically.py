class Solution(object):
    def printVertically(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        answer=[]
        s=s.split()
        max_length_string = len(max(s, key=len))
        for i in range(max_length_string):
            w=""
            for word in s:
                if i < len(word):
                    w+=word[i]
                else:
                    w+=" "
                    # if len(w) >=1:
                    #     if w[-1] == " ":
                    # else:
                    #        w+=" "
            answer.append(w)
        for i in range(len(answer)):
            while answer[i][-1] == " ":
                answer[i]=answer[i][:-1]
        return answer