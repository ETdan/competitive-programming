# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict={}
        for a in strs:
            if ''.join(sorted(a)) in dict:
                dict[''.join(sorted(a))]+= " " + a
            else:
                dict[''.join(sorted(a))]=a

        answer=[]
        
        dict_to_eliminate_repetition={}
        for i in range(len(strs)):
            a=''.join(sorted(strs[i]))
            if a not in dict_to_eliminate_repetition:
                val=dict[a]
                answer.append(val.split(' '))
                dict_to_eliminate_repetition[a]=1

        return answer