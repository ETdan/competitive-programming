class OrderedStream(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.n=n
        self.arr=[[0]*2]*n
        self.ptr=0

    def insert(self, idKey, value):
        """
        :type idKey: int
        :type value: str
        :rtype: List[str]
        """
        answer=[]
        self.arr[idKey-1] = [idKey,value]

        while self.ptr <= self.n-1:
            if self.arr[self.ptr][0] != 0: 
                answer.append(self.arr[self.ptr][1])
                self.ptr+=1
            else:
                break
                
        return answer
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)