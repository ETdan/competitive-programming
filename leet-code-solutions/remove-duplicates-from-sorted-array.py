class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seeker=0
        holder=0

        while seeker < len(nums):
            if nums[holder] == nums[seeker]:
                seeker+=1
            else:
                nums[holder + 1] = nums[seeker]
                holder += 1


        return holder + 1