class Bitset(object):

    def __init__(self, size):
        """
        :type size: int
        """
        self.n=size
        
        self.bit0=[0]*self.n
        self.bit1=[1]*self.n
        
        self.count_=0

    def fix(self, idx):
        """
        :type idx: int
        :rtype: None
        """
        
        if self.bit0[idx] == 0:
            self.bit0[idx] = 1
            self.bit1[idx] = 0
            self.count_+=1

    def unfix(self, idx):
        """
        :type idx: int
        :rtype: None
        """

        if self.bit0[idx] == 1:
            self.bit0[idx]=0
            self.bit1[idx]=1
            if self.count_ > 0:
                self.count_-=1        

    def flip(self):
        """
        :rtype: None
        """

        self.bit0 ,self.bit1 = self.bit1 ,self.bit0
        self.count_= self.n - self.count_

    def all(self):
        """
        :rtype: bool
        """

        if self.count_ == self.n:
            return True
        else:
            return False

    def one(self):
        """
        :rtype: bool
        """

        if self.count_ >0:
            return True
        else:
            return False        

    def count(self):
        """
        :rtype: int
        """
        return self.count_

    def toString(self):
        """
        :rtype: str
        """
        return "".join([str(bit) for bit in self.bit0])

# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count_()
# param_7 = obj.toString()