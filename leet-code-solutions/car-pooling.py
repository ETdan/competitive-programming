class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        max_val=0
        for num_of_pass,start,end in trips:
            max_val=max(max_val,end)
        answer=[0]*max_val

        for num_of_pass,start,end in trips:
            answer[start]+=num_of_pass
            
            if end<max_val:
                answer[end]-=num_of_pass
        
        
        for i in range(1,len(answer)):
            answer[i]+=answer[i-1]
        # print(answer)
        
        return max(answer) <= capacity