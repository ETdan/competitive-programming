class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        answer=[]
        nums.sort()

        for i in range(len(nums)):
            first_val=nums[i]
            left=0
            right=len(nums)-1
            # print(first_val,"here")

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
                    values=[first_val,nums[left],nums[right]]
                    # print(values)

                    if first_val + nums[left] + nums[right] == target:
                        return target
                    elif first_val + nums[left] + nums[right] < target:
                        left += 1
                    elif first_val + nums[left] + nums[right] > target:
                        right-=1
        
                    answer.append(sum(values))
        

        sum_=0
        min_=float('inf')
        for val in answer:
            if abs(target - val) < min_:
                min_ = abs(target - val)
                sum_=val
        
        return sum_
                