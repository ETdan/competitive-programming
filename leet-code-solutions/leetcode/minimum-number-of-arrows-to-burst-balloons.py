class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # sort with the end val
        # if end val of curr is >= start val of next continue
        # else add to arrow counter

        points.sort(key=lambda x: x[1])

        arrow_counter=1
        curr=points[0][1]
        for i in range(len(points)-1):
            # print(points[i][1],points[i+1][0])
            if curr>=points[i+1][0]:
                continue
            # print("here")
            curr=points[i+1][1]
            arrow_counter+=1

        return arrow_counter