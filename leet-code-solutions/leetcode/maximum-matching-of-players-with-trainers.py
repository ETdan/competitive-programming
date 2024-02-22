class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()

        p=t=pairs=0

        while p < len(players) and t < len(trainers):
            if players[p] <= trainers[t]:
                pairs+=1
                p+=1
            
            t+=1

        return pairs


