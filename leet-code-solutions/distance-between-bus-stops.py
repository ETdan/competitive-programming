class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """

        s=sum(distance)

        if destination<start:
            destination, start = start, destination
        local_sum=0
        for i in range(start,destination):
            local_sum+= distance[i%len(distance)]
            
        return min(s - local_sum, local_sum)
        