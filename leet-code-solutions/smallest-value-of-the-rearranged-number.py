class Solution:
    def smallestNumber(self, num: int) -> int:
        nums=[]
        negative=False

        # make the number posetive
        if num < 0:
            negative=True
            num=0-num
        
        while num > 0:
            nums.append(str(num%10))
            num=num//10

        # sort in increasing order
        def helper(num1,num2):
            if int(num1 + num2) > int(num2 + num1):
                return [num2, num1]
            else:
                return [num1, num2]
        
        # sort in decreasing order
        def negative_helper(num1,num2):
            if int(num1 + num2) < int(num2 + num1):
                return [num2, num1]
            else:
                return [num1, num2]

        if negative:
            for i in range(len(nums)):
                for j in range(len(nums)-1-i):
                    nums[j], nums[j+1] = negative_helper(nums[j],nums[j+1])
        else:   
            for i in range(len(nums)):
                for j in range(len(nums)-1-i):
                    nums[j], nums[j+1] = helper(nums[j],nums[j+1])

            # swap leading zero with the first non-zero element
            if len(nums) > 0:
                if nums[0] == '0':
                    for i in range(len(nums)):
                        if nums[i] != '0':
                            nums[0]=nums[i]
                            nums[i] = '0'
                            break

        answer="".join(nums)

        if answer == '':
            return 0

        if negative:
            return 0-int(answer)
        else:
            return int(answer)