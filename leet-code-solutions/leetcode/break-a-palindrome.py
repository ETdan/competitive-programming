class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        def is_palindrome(word):
            for i in range(len(word)//2):
                if word[i] != word[len(word)-i-1]:
                    return False
            
            return True

        p = palindrome[(len(palindrome)//2):]

        if palindrome == "" or len(palindrome) == 1:
            return ""
        
        alpha=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        answer=[]
        
        for index,char in enumerate(palindrome):
            i=0
            while char == alpha[i]:
                i+=1
                
            if index == 0:
                print("0")
                temp = alpha[i] + palindrome[1:]
            elif index == len(palindrome)-1:
                print("-1")
                temp = palindrome[:-1] + alpha[i] 
            else:
                print("here")
                temp = palindrome[:index-1] + alpha[i] + palindrome[index:]
            if temp != palindrome:
                answer.append(temp)
        answer=sorted(answer)
        print(answer)

        if len(answer) == 0:
            return ""
        for i in range(len(answer)):
            if not is_palindrome(answer[i]):
                return answer[i]
        return ""
        