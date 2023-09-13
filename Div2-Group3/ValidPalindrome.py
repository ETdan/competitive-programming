class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        word=""
        left=0
        right=len(s)-1
        while left < right:
            a = s[left]
            b = s[right]
            print(a,b)
            if a.isalnum() and b.isalnum():
                if a.lower() == b.lower():
                    left += 1
                    right -= 1
                    continue
                else:
                    return False
            if not a.isalnum():
                print(a)
                left += 1
            if not b.isalnum():
                right -= 1
        return True
        # for letter in s:
        #     if letter.isalnum():
        #         if letter.isdigit():
        #             word += letter
        #         else:
        #             word += letter.lower()

        # word_reverse=word[::-1]
        # return word == word_reverse
        
