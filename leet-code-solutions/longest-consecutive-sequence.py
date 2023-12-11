class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        visited=set()
        nums_set=set(nums)

        max_sequence=0


        for element in nums_set:
            sequence=1
            num=element
            if num not in visited:
                visited.add(element)
                # to the right of element
                while num in nums_set:
                    if num+1 in nums_set:
                        visited.add(num)
                        sequence+=1
                    num+=1

                # to the left of element
                while num in nums_set:
                    if num - 1 in nums_set:
                        visited.add(num)
                        sequence+=1
                    num-=1
            max_sequence=max(max_sequence,sequence)      
            
        return max_sequence