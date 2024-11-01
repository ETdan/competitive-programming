# Problem: Map Sum Pairs - https://leetcode.com/problems/map-sum-pairs/description/

class MapSum:

    def __init__(self):
        self.map=defaultdict(int)

    def insert(self, key: str, val: int) -> None: 
        self.map[key]=val
        
    def sum(self, prefix: str) -> int:
        answer=0
        for key,val in self.map.items():
            pos=key.find(prefix)
            if pos==0:
                answer+=val
        return answer


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)