class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==1: return strs[0]
        min_length = len(min(strs, key=len))
        if min_length == 0:
            return ""
        j=min_length
        common=strs[0][:j]
        for i in range(1,len(strs)):
            for k in range(j):
                if common[k] != strs[i][k]:
                    if k==0:
                        return ""
                    j=k
                    break
            common=common[:j]
        
        return common
        