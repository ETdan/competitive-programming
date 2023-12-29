class Solution:
    def sortSentence(self, s: str) -> str:
        answer=[""]*(s.count(" ")+1)
        current_index=0

        # loop through s
        while current_index < len(s):
            current_word=""

            # if the current char is not a spacse or or a digit it will increment current_index
            while s[current_index] != " " and not s[current_index].isdigit():
                current_word+=s[current_index]
                current_index+=1

            # if the current char is a digit it will add to answer if the the current char is a digit 
            if s[current_index].isdigit():
                answer[int(s[current_index])-1]=current_word

            current_index+=1
            
        return " ".join(answer)