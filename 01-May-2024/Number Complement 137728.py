# Problem: Number Complement - https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        num = bin(num)
        answer=[]
        for i in range(2,len(num)):
            if num[i] == '0':
                answer.append('1')
            else:
                answer.append('0')
        
        return int(''.join(answer),2)