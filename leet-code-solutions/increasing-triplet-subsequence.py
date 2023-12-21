class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        x=float("inf")
        y=float("inf")
        z=float("inf")

        for i in range(len(nums)):
            if nums[i] > x:
                if nums[i] > y:
                    if  nums[i] > z:
                        # print("here")
                        return True
                    else:
                        z=nums[i]
                else:
                    y=nums[i]
            else:
                x=nums[i]
        if x < y < z and max(x,y,z) != float("inf") :
            # print(x,y,z)
            return True
        
        return False