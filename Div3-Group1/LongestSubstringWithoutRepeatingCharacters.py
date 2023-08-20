class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxLen=0
        left=0
        dict={}
        for i in range(len(s)):
            c = s[i]
            if c in dict and dict[c] >= left:
                left = dict[c] + 1
                dict[c] = i
            else:
                dict[c]=i
                maxLen=max(maxLen , i - left + 1 )

        return maxLen
