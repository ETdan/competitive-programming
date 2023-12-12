class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visited=set()

        while n != 1:
            temp=0
            if n in visited:
                break
            visited.add(n)
            while n != 0:
                temp+=pow((n%10),2)
                n/=10
            n=temp
        
        if n==1:
            return True
        else:
            return False
        