# Problem: Count the Number of Consistent Strings - https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        answer=0
        for word in words:
            for char in word:
                if char not in allowed:
                    break
            else:
                answer+=1
        
        return answer