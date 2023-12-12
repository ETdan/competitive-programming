class UndergroundSystem(object):

    def __init__(self):
        self.checkIn_dict=defaultdict(list)
        self.average_dict=defaultdict(list)
        

    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.checkIn_dict[id]=[stationName,t]

        

    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        if (self.checkIn_dict[id][0],stationName) in self.average_dict:
            self.average_dict[(self.checkIn_dict[id][0],stationName)].append(t - self.checkIn_dict[id][1])
        else:
            self.average_dict[(self.checkIn_dict[id][0],stationName)]=[(t - self.checkIn_dict[id][1])]

    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        # print(sum(self.average_dict[(startStation,endStation)]),sum(self.average_dict[(startStation,endStation)]))
        return (float(sum(self.average_dict[(startStation,endStation)]))/len(self.average_dict[(startStation,endStation)]))
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)