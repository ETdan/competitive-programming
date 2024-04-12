# Problem: Broken Calculator - https://leetcode.com/problems/broken-calculator/description/

class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:

        turn = 0
        if startValue >= target:
            return startValue-target
             
        if startValue >= ceil(target/2):
            turn = startValue-ceil(target/2) 
            turn += abs((ceil(target/2) * 2) - target)  + 1
            return turn 
        
        stack=[]

        while startValue < ceil(target/2):
            stack.append(target)
            target =ceil(target/2)
        
        stack.append(target)

        while stack:
            target = stack.pop()
            turn += startValue-ceil(target/2) 
            turn += abs((ceil(target/2) * 2) - target)  + 1
            # print(target,startValue,turn)
            startValue = target
        
        return turn
