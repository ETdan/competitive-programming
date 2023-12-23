class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) <= 2:
            return False
       
        index = 0
        for i in range(len(arr)-1):
            if arr[i] >= arr[i+1]:
                index = i
                break
        
        for i in range(index, len(arr)-1):
            if arr[i] <= arr[i+1]:
                return False

        # print(index)
        return index != 0