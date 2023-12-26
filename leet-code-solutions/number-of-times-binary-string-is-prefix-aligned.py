class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        arr=[0]*len(flips)
        j=0
        answer = 0

        for i in range(len(flips)):
            arr[flips[i]-1]=1
            if arr[j] == 1:
                while j < len(flips) and arr[j] == 1:
                    j += 1
            if i < j:
                # print(answer,j,i) 
                answer += 1
        return answer