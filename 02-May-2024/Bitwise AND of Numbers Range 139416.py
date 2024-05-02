# Problem: Bitwise AND of Numbers Range - https://leetcode.com/problems/bitwise-and-of-numbers-range/

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        
        if left == right:
            return left & right
        
        
        answer = ''
        left = bin(left)[2:]
        right = bin(right)[2:]

        diff = len(right) - len(left)
        
        while diff:
            answer+='0'
            diff-=1

        # answer.extend(left)
        left=answer + left

        answer=[]
        # print(left,right)
        for i in range(len(left)):
            if left[i] == '1' and right[i]=='1':
                # print(int(right[:i] +'0' +right[i+1:],2),i,right[:i], '0' ,right[i+1:])
                if int(left,2) <= int(right[:i] +'0' +right[i+1:],2) <=int(right,2):
                    answer.append('0')
                else:
                    answer.append('1')
            else:
                answer.append('0')

        answer = ''.join(answer)

        return int(answer,2)
