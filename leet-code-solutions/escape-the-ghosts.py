class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        distance_to_goal=(abs(target[0])+abs(target[1]))
        x2=target[0]
        y2=target[1]
        
        for i in range(len(ghosts)):
            x1=ghosts[i][0]
            y1=ghosts[i][1]
            x=abs(x2-x1)
            y=abs(y2-y1)
            
            if distance_to_goal >= x + y:
                return False

        return True