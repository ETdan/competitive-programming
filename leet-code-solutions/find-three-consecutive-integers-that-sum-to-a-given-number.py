class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        max=num//3

        for i in range(max-3,max+3):
            if (i*3)+3 == num:
                return [i,i+1,i+2]
        return []