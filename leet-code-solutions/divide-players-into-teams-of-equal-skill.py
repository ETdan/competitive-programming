class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        sum_=skill[0] + skill[-1]
        answer = 0
        left=0
        right=len(skill)-1

        while left < right:
            if sum_ == skill[left] + skill[right]:
                answer+= skill[left] * skill[right]
            else:
                return -1
            
            left+=1
            right-=1

        return answer