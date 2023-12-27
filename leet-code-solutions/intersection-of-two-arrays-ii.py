class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        Dict1= {}
        Dict2= {}
        answer=[]
        for num in nums1:
            Dict1[num] = Dict1.get(num, 0) + 1

        for num in nums2:
            Dict2[num] = Dict2.get(num, 0) + 1
        # print(sorted(nums1), sorted(nums2), Dict1, Dict2)
        for key,val in Dict1.items():
            # print(key, val)
            if key in Dict2:
                # print(key, val, Dict2[num])
                for i in range(min(val,Dict2[key])):
                    answer.append(key)

        return answer
