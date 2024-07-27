# Problem: Sort the Jumbled Numbers - https://leetcode.com/problems/sort-the-jumbled-numbers/

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        answer=[]
        for num in nums:
            new_num=""
            for char in str(num):
                new_num+=str(mapping[int(char)])
            answer.append([num,int(new_num)])
        
        answer.sort(key=lambda x:x[1])
        
        return [x for x,y in answer]