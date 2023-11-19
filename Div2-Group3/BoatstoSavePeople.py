class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        boat=0

        left=0
        right=len(people)-1

        # if sum(people) <=limit:
        #     return 1
        
        while left <= right:
            if left == right:
                if left + 1 >= len(people):
                    right-=1
                else:
                    left+=1
                boat+=1
            else:
                if people[left] + people[right] <= limit:
                    boat+=1
                    left+=1
                    right-=1
                elif people[left] + people[right] > limit:
                    boat+=1
                    right-=1
        return boat
