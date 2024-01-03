class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boat=0

        left=0
        right=len(people)-1
        
        while left <= right:
            if left == right:
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