class Solution(object):
    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """
        bad=set()
        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                bad.add(fronts[i])
        good=set()

        for i in range(len(fronts)):
            if fronts[i] not in bad:
                good.add(fronts[i])
            if backs[i] not in bad:
                good.add(backs[i])
        if len(good) == 0: 
            return 0
        return min(list(good))