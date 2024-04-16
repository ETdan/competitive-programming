# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        for i in range(len(piles)):
            piles[i]*=-1

        heapq.heapify(piles)
        
        while k:
            if piles:
                largest = heapq.heappop(piles)
                heapq.heappush(piles,largest//2)
            else:
                break
            k -= 1
        
        return sum(piles)*-1