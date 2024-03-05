class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters=["abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        if digits == "":
            return []
        if len(digits) == 1:
            return letters[int(digits)-2]

        answer = []
        temp = []

        # for i in range(len(digits)):
        #     for j in range(i+1,len(digits)):
        #         # print( letters[int(digits[i])-2], letters[int(digits[j])-2])
        #         for char1 in letters[int(digits[i])-2]:
        #             for char2 in letters[int(digits[j])-2]:
        #                 answer.append(char1 + char2)

        def backTrack(char,digit_index):
            # print(char,digits[digit_index])
            # print(temp)
            if len(temp) == len(digits):
                answer.append("".join(temp))
                return
            if digit_index == len(digits):
                return
            
            for i,char in enumerate(letters[int(digits[digit_index])-2]):
                temp.append(char)
                backTrack(char,digit_index + 1)
                temp.pop()

        
        for index,char in enumerate(letters[int(digits[0])-2]):
            temp.append(char)
            backTrack(char,1)
            temp.pop()


        return answer