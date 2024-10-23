# Problem: Find the Index of the first occurence - https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i=0
        j=0
        temp=0

        while i < len(haystack) and temp < len(haystack) and j < len(needle):
            if haystack[temp] == needle[j]  and j < len(needle)-1:
                temp+=1 
                j+=1
            elif haystack[temp] == needle[j] and j == len(needle)-1:
                return i
            else:
                j=0
                i+=1
                temp=i

        return -1