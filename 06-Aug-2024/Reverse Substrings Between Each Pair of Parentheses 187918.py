# Problem: Reverse Substrings Between Each Pair of Parentheses - https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        answer=[]

        for char in s:
            if char == '(':
                answer.append('')
            elif char == ')':
                answer[-1]=answer[-1][::-1]
                if len(answer) > 1:
                    x=answer.pop()
                    answer[-1]+=x
            else:
                if len(answer) >= 1:
                    answer[-1]+=char
                else:
                    answer.append(char)
            # print(answer)
        # print(answer)

        return ''.join(answer)