class Solution(object):
    def wateringPlants(self, plants, capacity):
        """
        :type plants: List[int]
        :type capacity: int
        :rtype: int
        """
        c = capacity
        step=0

        for i in range(len(plants)):
            if plants[i] <= c:
                step += 1
                c -= plants[i]
            else:
                c = capacity-plants[i]
                step += (i+i+1)

            # print(plants[i],c)

        return step