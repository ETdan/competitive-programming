class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        arr=[] #stores the sum of two consecutive numbers 
        for i in range(len(weights)-1):
            arr.append(weights[i]+weights[i+1])
        arr.sort()
        
        maxs=0
        mins=0

        for i in range(k-1): # we do k-1 for some reason
            maxs+=arr[len(arr)-i-1]
            mins+=arr[i]
        
        return maxs - mins
