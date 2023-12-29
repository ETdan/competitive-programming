class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        curr=0
        answer = 0

        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                curr+=1
                answer+=curr
            else:
                answer+=curr
            # print(curr)
        return answer




        # max_to_min=[]
        # max_to_min_set=set()
        
        # nums.sort()

        # for i in range(len(nums)-1,-1,-1):
        #     if nums[i] not in max_to_min_set:
        #         max_to_min.append(nums[i])
        #         max_to_min_set.add(nums[i])
        # j=0
        # counter=0

        # while j < len(max_to_min):
        #     for i in range(len(nums)-1,-1,-1):
        #         if nums[i] > max_to_min[j]:
        #             # print("b",j,max_to_min[j],nums[i])
        #             nums[i]=max_to_min[j]
        #             counter+=1
        #             # print("a",j,max_to_min[j],nums[i])
        #     # print("here")
        #     j+=1
        #     # max_to_min[j]=max_to_min[j]
        #     # print(nums)
        # return counter