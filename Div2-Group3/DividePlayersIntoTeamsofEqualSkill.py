class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        skill.sort()
        target = skill[0] + skill[-1]
        # print(target)

        left =0
        right=len(skill)-1
        chem=0

        for _ in range((right+1)/2):
            if skill[left] + skill[right] == target:
                # print(skill[left], skill[right])
                chem += skill[left]*skill[right]
                left+=1
                right-=1
            else:
                return -1
        return chem
