class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        count_of_p=defaultdict(int)
        for char in p:
            count_of_p[char]+=1

        left=0
        right=len(p)
        answer=[]

        while left < len(s) - len(p) + 1:
            count_of_s_interval=defaultdict(int)
            
            for char in s[left:right]:
                count_of_s_interval[char]+=1
            
            if count_of_s_interval == count_of_p:
                answer.append(left)

            left+=1
            right+=1

        return answer
