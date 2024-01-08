class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels=('a','e','i','o','u')
        max_vowel_count=0
        temp_vowel_count=0

        left=0
        right=0


        for  right in range(len(s)):
            if s[right] in vowels:
                temp_vowel_count+=1

            if right - left + 1 >k:
                if s[left] in vowels:
                    temp_vowel_count-=1
                left += 1

            max_vowel_count=max(max_vowel_count,temp_vowel_count)


        return max_vowel_count