class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        counter=i=0

        while tickets[k]>0:
            if tickets[i%len(tickets)] > 0:
                counter+=1
                tickets[i%len(tickets)]-=1
            i+=1
        return counter