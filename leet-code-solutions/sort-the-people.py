class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        Dict={}

        for i in range(len(names)):
            Dict[heights[i]]=names[i]
        
        for i in range(len(names)):
            for j in range(len(names)-i-1):
                if heights[j] < heights[j+1]:
                    heights[j] , heights[j+1] =  heights[j+1], heights[j]

        return [Dict[height] for height in heights]