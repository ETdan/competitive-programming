class Solution:
    def bestClosingTime(self, customers: str) -> int:
        bestTime, penaltyDiff = 0, 0
            
        for i in range(0, len(customers)):
            if customers[i] == 'Y':
                penaltyDiff -= 1
            else:
                penaltyDiff += 1
            
            if penaltyDiff < 0:
                penaltyDiff = 0
                bestTime = i + 1
        return bestTime