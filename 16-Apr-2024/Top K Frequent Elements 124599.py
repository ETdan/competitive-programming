# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict={}
        for a in nums:
            if a in my_dict:
                my_dict[a]+=1
            else:
                my_dict[a]=1
        
        my_dict=sorted(my_dict, key=my_dict.get, reverse=True)
        
        answer=[]
        for a in my_dict:
            k-=1
            answer.append(a)
            if k==0:
                break

        return answer