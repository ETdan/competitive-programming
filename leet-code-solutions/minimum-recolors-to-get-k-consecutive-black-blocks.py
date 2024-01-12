class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_recolor = blocks[:k].count("W")
        # print(min_recolor,len(blocks[:k]),blocks[:k],blocks[k])
        left=0
        temp_min = min_recolor


        for right in range(k,len(blocks)):

            if blocks[right] == "W":
                temp_min += 1
            
            if blocks[left] == "W":
                if temp_min > 0:
                    temp_min -= 1

            # print(blocks[left],blocks[right],temp_min)

            left+=1
            
            min_recolor = min(temp_min, min_recolor)
            
        return min_recolor
