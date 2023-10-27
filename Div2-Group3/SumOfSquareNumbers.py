class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        maxValue=int(math.sqrt(c))
        minValue=0
        value=minValue**2 + maxValue**2

        while minValue<=maxValue:
            if value == c:
                return True
            elif value < c:
                minValue+=1
            else:
                maxValue-=1
            value=minValue**2 + maxValue**2
        return False
