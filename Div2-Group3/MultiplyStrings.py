class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if "0" in [num1,num2]:
            return "0"
        
        answer = [0]*(len(num1)+len(num2))
        num1=list(num1)[::-1]
        num2=list(num2)[::-1]

        for ia,a in enumerate(num2):
            for ib,b in enumerate(num1):
                val = int(a) * int(b)
                carry = val / 10 
                val = val % 10

                answer[ia+ib] += val 
                answer[ia+ib+1] += carry 

                answerCarry = answer[ia+ib] / 10 
                if answerCarry != 0:
                    answer[ia+ib] %= 10 
                    answer[ia+ib+1] += answerCarry 
                    
        answer = answer[::-1]
        index = 0
        for num in answer:
            if num != 0:
                break
            index+=1
        
        answer = answer [index:]
        return ''.join(str(num) for num in answer)
