class Solution(object):
    def checkPowersOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def closer(n):
            m=0
            i=0
            while m <= n:
                if pow(3,i) > n:
                    return [(i-1),pow(3,(i-1))]
                else:
                    i+=1

            return [i,pow(3,i)]
        index=[]
        while n:
            [i,m]=closer(n)
            n-=m
            # print(m,n,i)
            if i in index:
                return False
            else:
                index.append(i)
        return True


        