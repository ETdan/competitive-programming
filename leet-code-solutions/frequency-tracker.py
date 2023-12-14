class FrequencyTracker(object):

    def __init__(self):
        self.Dict=defaultdict(int)
        self.fdict=defaultdict(int)
        
    def add(self, number):
        """
        :type number: int
        :rtype: None
        """
        
        if self.Dict[number] in self.fdict:
            if self.fdict[self.Dict[number]] <= 1:
                del self.fdict[self.Dict[number]]
            else:
                self.fdict[self.Dict[number]]-=1
                
        self.Dict[number]+=1
        self.fdict[self.Dict[number]]+=1
        

    def deleteOne(self, number):
        """
        :type number: int
        :rtype: None
        """
        if number in self.Dict:
            if self.Dict[number] == 1:
                del self.Dict[number]
                if self.fdict[1] == 1:
                    del self.fdict[1]
                else:
                    self.fdict[1] -=1
            else:
                if self.Dict[number] in self.fdict:
                    if self.fdict[self.Dict[number]] <= 1:
                        del self.fdict[self.Dict[number]]
                    else:
                        self.fdict[self.Dict[number]]-=1

                self.Dict[number]-=1
                self.fdict[self.Dict[number]]+=1
        

    def hasFrequency(self, frequency):
        """
        :type frequency: int
        :rtype: bool
        """
        if frequency in self.fdict:
            return True
        
        return False
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)