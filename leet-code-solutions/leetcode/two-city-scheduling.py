class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        cost=0
        
        costs.sort(key=lambda x:x[0]-x[1])
        
        for i in range(len(costs)//2):
            cost+=costs[i][0]
        for i in range(len(costs)//2,len(costs)):
            cost+=costs[i][1]

        return cost