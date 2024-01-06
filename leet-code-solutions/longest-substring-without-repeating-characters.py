class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest=0
        left=0
        breaked=False

        while left < len(s):
            curent=set()
            temp_length=0
            temp=left

            while s[temp] not in curent:
                temp_length+=1
                curent.add(s[temp])
                temp+=1

                if temp >= len(s):
                    longest = max(longest,temp_length)
                    breaked=True
                    break 
            if breaked:
                break 
            
            longest = max(longest,temp_length)
            left+=1
        
        return longest