class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer=[]
        temp=[]
        seen_index=set()

        def backTrack(curr_index):
            if len(temp) == len(nums):
                answer.append(temp[:])
                return

            for i in range(len(nums)):
                if i not in seen_index:
                    seen_index.add(i)
                    temp.append(nums[i])
                    backTrack(i+1)
                    temp.pop()
                    seen_index.remove(i)

        backTrack(0)

        return answer