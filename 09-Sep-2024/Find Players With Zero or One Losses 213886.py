# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners=[]
        lossers=[]
        Dict={}

        # preparing Dict to have all players
        for winner,losser in matches:
            if winner not in Dict:
                Dict[winner]=[0,0]
            if losser not in Dict:
                Dict[losser]=[0,0]
            
        # count all players win and loss
        for winner,losser in matches:
            if winner in Dict:
                Dict[winner][0]+=1

            if losser in Dict:
                Dict[losser][1]+=1

        # cecking win and loss to make the answer
        for key,value in Dict.items():
            if value[1] == 0:
                winners.append(key)
            if value[1] == 1:
                lossers.append(key)
        
        return [sorted(winners),sorted(lossers)]