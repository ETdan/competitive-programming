class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        firstList_pointer=0
        secondList_pointer=0
        answer=[]

        while firstList_pointer < len(firstList) and secondList_pointer < len(secondList):
            left_end=max(firstList[firstList_pointer][0],secondList[secondList_pointer][0])
            right_end=min(firstList[firstList_pointer][1],secondList[secondList_pointer][1])

            if left_end <= right_end:
                answer.append([left_end,right_end])
            
            if firstList[firstList_pointer][1] <secondList[secondList_pointer][1]:
                firstList_pointer += 1
            else:
                secondList_pointer += 1
        return answer