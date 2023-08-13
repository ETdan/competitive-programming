class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort()
        sum=0
        for a in range(len(piles)-1,(len(piles)/3),-2):
            sum+=piles[a-1]
        return sum
