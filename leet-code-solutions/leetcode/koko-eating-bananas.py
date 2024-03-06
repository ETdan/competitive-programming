class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right=min_hour = sum(piles)
        mid=(left+right)//2

        def rateIsValid(rate):
            temp= rate
            hour_taken=0
            for i in range(len(piles)):
                hour_taken += ceil(piles[i]/rate)
            
            return hour_taken<=h
        
        while left <= right:
            if rateIsValid(mid):
                min_hour= min(min_hour,mid)
                right=mid-1
            else:
                left=mid+1
            mid = (left + right) // 2

        return min_hour