class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_candie=max(candies)
        answer=[False]*len(candies)

        for i,candie in enumerate(candies):
            if candie + extraCandies >=max_candie:
                answer[i]=True
        return answer

        