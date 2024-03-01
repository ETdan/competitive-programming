class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        def recur(l, r, Turn):
            if Turn:
                if l == r:
                    return nums[l]
                
                left = recur(l+1,r,not Turn) + nums[l]
                right = recur(l,r-1,not Turn) + nums[r]

                return max(left,right)
            else:
                if l == r:
                    return 0 - nums[l]
                
                left = recur(l+1,r,not Turn) - nums[l]
                right = recur(l,r-1,not Turn) - nums[r]

                return min(left,right)

        return recur(0,len(nums)-1,True) >= 0
