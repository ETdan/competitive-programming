class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        answer=[]
        def flip(arr,k):
            for i in range(k//2):
                arr[i], arr[k-i-1] = arr[k-i-1], arr[i]
            return arr

        max_element=len(arr)

        while max_element > 0:
            index_of_max_element = arr.index(max_element)
            
            answer.append(index_of_max_element + 1)
            
            arr =flip(arr,index_of_max_element + 1)
            
            answer.append(max_element)
            arr =flip(arr,max_element)
            
            max_element-=1


        return answer