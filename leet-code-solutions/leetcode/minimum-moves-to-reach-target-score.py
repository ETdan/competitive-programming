class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        counter = 0
        while target:
            if maxDoubles and target % 2 == 0:
                target /= 2
                maxDoubles-=1
            elif maxDoubles and target % 2 != 0:
                target -= 1
            else:
                counter+=(target)
                break
            
            counter += 1
        return int(counter-1)
