class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        word=""
        for letter in s:
            if letter.isalnum():
                if letter.isdigit():
                    word += letter
                else:
                    word += letter.lower()
                    
        word_reverse=word[::-1]
        return word == word_reverse
