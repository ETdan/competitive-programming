class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        common=-1
        left=0
        right=0

        while left < len(nums1) and right < len(nums2):
            if nums1[left] == nums2[right]:
                common = nums1[left]
                break
            elif nums1[left] < nums2[right]:
                 left+=1
            else:
                 right+=1
                 
        return common