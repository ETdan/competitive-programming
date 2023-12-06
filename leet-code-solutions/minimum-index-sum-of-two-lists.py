class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """

        Dict={}
        answer=[]
        
        least_index_sum=2000

        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] not in Dict:
                    if list1[i] == list2[j]:
                        if least_index_sum > i+j:
                            least_index_sum = i+j

                        Dict[list1[i]]=i+j
        
        for key,value in Dict.items():
            if value == least_index_sum:
                answer.append(key)
        
        return answer
                        