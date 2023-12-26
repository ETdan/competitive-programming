class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        Dict=defaultdict(int) # to store repetition
        answer=[]
        for num in arr1:
            Dict[num]+=1

        for num in arr2:
            frequecy=Dict[num]
            while frequecy:
                answer.append(num)
                frequecy-=1

            Dict[num] = 0
        leftout=[]
        for key,val in Dict.items():
            if val !=0:
                while val:
                    leftout.append(key)
                    val-=1
        leftout.sort()
        answer.extend(leftout)
        return answer