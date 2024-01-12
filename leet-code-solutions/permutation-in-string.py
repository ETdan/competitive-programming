class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)

        if k > len(s2):
            return False

        count_of_s1=defaultdict(int)
        count_of_s2=defaultdict(int)

        for i in range(len(s1)):
            count_of_s1[s1[i]]+=1
            count_of_s2[s2[i]]+=1
        
        # count_of_s1[s1[-1]]+=1

        for i in range(k,len(s2)):

            if  count_of_s1 == count_of_s2:
                return True
            
            count_of_s2[s2[i]]+=1
            
            # print(s2[i-k])

            if count_of_s2[s2[i-k]] > 1:
                count_of_s2[s2[i-k]] -= 1
            else:
                del count_of_s2[s2[i-k]]

        
        if  count_of_s1 == count_of_s2:
            return True

        return False
