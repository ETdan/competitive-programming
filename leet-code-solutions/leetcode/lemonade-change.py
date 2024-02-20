class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change=[0,0,0]

        for bill in bills:
            if bill == 5:
                change[0]+=1
            elif bill == 10:
                if change[0] >=1:
                    change[0]-=1
                    change[1]+=1
                else:
                    return False
            else:
                if change[1] >=1 and change[0] >=1 :
                    change[0]-=1
                    change[1]-=1
                elif change[0] >=3 :
                    change[0]-=3
                else:
                    return False
        return True


            