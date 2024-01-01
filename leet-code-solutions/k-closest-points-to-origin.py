class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance=[]
        for point in points:
            distance.append([sqrt(pow(point[0],2)+pow(point[1],2)),point])
        # print(distance)
        distance.sort()
        # print(distance)
        distance = distance[:k]
        # print(distance)
        return [point for _,point in distance]