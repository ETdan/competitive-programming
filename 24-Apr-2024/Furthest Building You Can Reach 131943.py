# Problem: Furthest Building You Can Reach - https://leetcode.com/problems/furthest-building-you-can-reach/

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap=[]
        heapq.heapify(heap)
        
        for i in range(len(heights)-1):
            diff = heights[i+1] - heights[i]
            if diff > 0:
                if ladders:
                    heapq.heappush(heap,diff)
                    ladders-=1
                else:
                    heapq.heappush(heap,diff)
                    passed_diff = heapq.heappop(heap)
                    if passed_diff <= bricks: 
                        bricks -= passed_diff 
                    else:
                        return i
            
        return len(heights) - 1
