class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        a_to_i=['a','b','c','d','e','f','g','h','i']
        j_to_z=['j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        answer=""
        for i in range(len(s)):
            if s[i] != "#":
                answer+=a_to_i[int(s[i])-1]
            else:
                answer=answer[:-2]
                n=int(s[i-2]+s[i-1])
                answer+=j_to_z[n-10]
        return answer
                
                