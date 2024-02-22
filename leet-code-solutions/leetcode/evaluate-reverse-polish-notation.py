class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        operators=[ '+', '-', '*','/']
        
        for char in tokens:
            if char in operators:
                num2=stack.pop()
                num1=stack.pop()
                if char == '+':
                    stack.append(num1+num2)
                if char == '-':
                    stack.append(num1-num2)
                if char == '/':
                    if num1 < 0 and num2 < 0:
                        stack.append(abs(num1)//abs(num2))
                    elif num1 < 0 or num2 < 0:
                        stack.append(0-(abs(num1)//abs(num2)))
                    else:
                        stack.append(abs(num1)//abs(num2))
                     
                if char == '*':
                    stack.append(num1*num2)
            else:
                stack.append(int(char))
        
        return stack[-1]