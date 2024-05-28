# Problem: Solving Questions with Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        answer = [0] * len(questions)
        answer[-1] = questions[-1][0]

        for i in range(len(questions) - 2, -1, -1):
            num = 0
            if i + questions[i][1] + 1 < len(questions):
                num = answer[i + 1 + questions[i][1]]

            answer[i] = max(questions[i][0] + num, answer[i + 1])
        
        return answer[0]
