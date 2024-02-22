class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        answer = [-1] * len(nums2)

        for i in range(len(nums2)):
            while stack and nums2[stack[-1]] <= nums2[i]:
                index = stack.pop()
                answer[index] = i

            stack.append(i)

        ans=[]

        for i in range(len(nums1)):
            index=nums2.index(nums1[i])
            index=nums2[answer[index]] if answer[index] != -1 else -1
            ans.append(index)

        return ans
