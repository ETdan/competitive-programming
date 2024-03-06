class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = 1
        right = total_sum = smallest_weight = sum(weights)

        mid = (left + right) // 2

        def isValid_weight(weight):
            temp = weight
            day = 1

            for i in range(len(weights)):
                if temp - weights[i] >= 0:
                    temp -= weights[i]
                else:
                    day += 1
                    temp = weight - weights[i]
                    if temp < 0:
                        return False
                # print(temp,day,weight,weights[i],day<=days)

            return day <= days

        while left <= right:
            # print(mid)
            if isValid_weight(mid):
                smallest_weight = min(smallest_weight,mid)
                # print(smallest_weight)
                right = mid - 1
            else:
                left = mid + 1

            mid = (left + right) // 2

        return smallest_weight
