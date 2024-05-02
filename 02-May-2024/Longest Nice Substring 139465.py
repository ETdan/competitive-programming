# Problem: Longest Nice Substring - https://leetcode.com/problems/longest-nice-substring/

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        ans = ""

        def check(start,end):
            new_substring=s[start:end]
            for i in range(start,end):
                # print(s[i],s[end-1],(s[i].lower() in new_substring) and (s[i].upper() in new_substring))
                if not ((s[i].lower() in new_substring) and (s[i].upper() in new_substring)):
                    # print(s[i])
                    return False
            
            return True
        
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if check(i,j) and len(ans) < j-i:
                    ans = s[i:j]
            
            # print("ans",ans)
                
        return ans 