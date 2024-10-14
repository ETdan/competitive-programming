# Problem: Cheapest Flights Within K Stops - https://leetcode.com/problems/cheapest-flights-within-k-stops/

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prev=[float('inf')]*n
        prev[src]=0
        
        def BellmanFord(prev):

            for _ in range(k+1):
                curr = prev[:]

                for u, v, w in flights:
                    curr[v] = min(curr[v], prev[u]+w)
                
                prev = curr[:]

            return prev
        
        prev=BellmanFord(prev)
        
        if prev[dst] != float('inf'):
            return prev[dst]
        else:
            return -1        