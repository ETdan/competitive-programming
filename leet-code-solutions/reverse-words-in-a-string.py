class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list=s.split()
        s_list=s_list[::-1]

        return " ".join(s_list)
        