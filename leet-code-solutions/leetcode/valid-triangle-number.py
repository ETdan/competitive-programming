class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        num_of_valid_triangle = 0
        nums.sort()

        for k in range(2,len(nums)):
            i=0
            j=k-1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    num_of_valid_triangle += (j-i)
                    j-=1
                else:
                    i+=1
     
        
        
        
        # print("///////////////////////")
        # num_of_valid_triangle = 0
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         for k in range(j+1,len(nums)):
        #             if i !=j and j !=k and i !=k:
        #                 if (nums[i] + nums[j] > nums[k]and nums[j] + nums[k] > nums[i]and nums[k] + nums[i] > nums[j]):
        #                     # print(i,j,k,nums[i] + nums[left] > nums[right]and nums[left] + nums[right] > nums[i]and nums[right] + nums[i] > nums[left])
        #                     # temp=[nums[i], nums[j], nums[k]]
        #                     # num_of_valid_triangle.append(tuple(temp))
        #                     num_of_valid_triangle += 1

        # # print(num_of_valid_triangle)
        return num_of_valid_triangle
