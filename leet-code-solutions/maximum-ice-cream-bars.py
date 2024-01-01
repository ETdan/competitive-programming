class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        highest_price=max(costs)
        costs_sorted=[0]*highest_price

        for cost in costs:
            costs_sorted[cost-1] += 1

        count=0
        for i in range(len(costs_sorted)):
            if costs_sorted[i] !=0:
                for j in range(0,costs_sorted[i]):
                    if coins - (i+1) >= 0:
                        coins -= (i+1)
                        count+=1
                    else:
                        break
                # print(i+1,costs_sorted[i],coins)

        return count