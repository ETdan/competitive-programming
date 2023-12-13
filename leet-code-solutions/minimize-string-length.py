class Solution(object):
    def minimizedStringLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        Dict=defaultdict(int)

        for i in range(len(s)-1,-1,-1):
            Dict[s[i]]+=1

        # print(Dict)
        return len(Dict)