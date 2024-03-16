class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        maxRadiusSeen = 0
        heaters.sort()
        for i in range(len(houses)):
            left = 0
            right = len(heaters) - 1
            radiusReq = float('inf')
            while left < right:
                mid = (left + right) // 2
                if heaters[mid] == houses[i]:
                    radiusReq = 0
                    break
                elif heaters[mid] < houses[i]:
                    radiusReq = min(radiusReq, abs(heaters[mid] - houses[i]))
                    left = mid + 1
                else:
                    radiusReq = min(radiusReq, abs(heaters[mid] - houses[i]))
                    right = mid
            radiusReq = min(radiusReq, abs(heaters[left] - houses[i]))
            maxRadiusSeen = max(maxRadiusSeen, radiusReq)
        return(maxRadiusSeen)
                    
