class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer=set()
        nums.sort()

        for i in range(len(nums)):
            target=nums[i]
            left=0
            right=len(nums)-1

            while left < right:
                if left == i or right == i:
                    if left == i and left + 1 < len(nums):
                        left += 1
                    else:
                        break
                    if right == i and right - 1 > 0:
                        right -= 1
                    else:
                        break
                else:
                    if target + nums[left] + nums[right] == 0:
                        values=[target,nums[left],nums[right]]
                        values.sort()
                        answer.add(tuple(values))
                        left+=1
                        right-=1
                    elif target + nums[left] + nums[right] < 0:
                        left += 1
                    elif target + nums[left] + nums[right] > 0:
                        right-=1
                
        return list(answer)
                