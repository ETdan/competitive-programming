class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        answer=""
        max_len= max(len(word1),len(word2))
        for i in range(max_len):
            if i < len(word1):
                answer+=word1[i]
            if i < len(word2):
                answer+=word2[i]
        return answer