class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        Dict={}
        percent25=len(arr)*(0.25)
        for num in arr:
            if num in Dict:
                Dict[num]+=1
            else:
                Dict[num]=1

        for key,val in Dict.items():
            if val > percent25:
                return key
        