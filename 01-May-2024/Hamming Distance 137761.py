# Problem: Hamming Distance - https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        binx=bin(x)
        biny=bin(y)

        extended =['0','b']
        longer=0
        shorter=0

        if len(binx) < len(biny):
            diff = len(biny) - len(binx)
            shorter=binx
            longer=biny
        else:
            diff = len(binx) - len(biny)
            shorter=biny
            longer=binx

        while diff:
            extended.append('0')
            diff-=1

        for i in range(2,len(shorter)):
            extended.append(shorter[i])
        
        answer =0
        # print(extended,shorter,longer,binx,biny,diff)
        for i in range(2,len(extended)):
            if extended[i] != longer[i]:
                answer+=1
        
        return answer