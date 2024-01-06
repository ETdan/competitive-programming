class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        
        for i in range(len(nums)):
            prev=i
            indices=set()
            index=prev

            was_posetive = nums[i] > 0
            sign_missmatch=False

            while index not in indices:
                if was_posetive != (nums[index] > 0):
                    sign_missmatch=True
                    break
                
                indices.add(index)
                index,prev = ((index + nums[index]) % len(nums)), index
                
            
            
            if not sign_missmatch and len(indices) > 1:
                # print(index,prev,i,"here")
                if prev == index:
                    return False
                return True

        return  False