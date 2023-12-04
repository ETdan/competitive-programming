class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if "0" in [num1,num2]:
            return "0"
        answer=[0]*(len(num1)+len(num2))

        num1,num2 = num1[::-1],num2[::-1]
        
        for i in range(len(num1)):
            for j in range(len(num2)):
                digit=int(num1[i])*int(num2[j])

                answer[i+j]+=digit
                answer[i+j+1]+=(answer[i+j])//10
                answer[i+j]=(answer[i+j])%10
        b=0
        answer=answer[::-1]
        for num in answer:
            if num==0:
                b+=1
            else:
                break
        answer= map(str,answer[b:])
        return ("".join(answer))