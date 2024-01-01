class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        sum_=0
        piles.sort()
        # print(piles)
        for i in range(len(piles)-1,(len(piles)//3),-2):
            sum_+=piles[i-1]
            # print(piles[i-1])
        return sum_