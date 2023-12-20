class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        counter=0

        for i in range(len(nums)-1,-1,-1):
            for j in range(i):
                if (j * i) % k == 0:
                    if nums[i] == nums[j]:
                        counter+=1
                        

        return counter 