class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        Sum=0
        counter=0
        while n:
            step=0
            counter+=1
            while step <=6 and n > 0:
                n-=1
                Sum+=(counter + step)
                step+=1
        return Sum