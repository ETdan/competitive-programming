class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        answer=[0]*len(boxes)
        boxes_list=[]

        # turn to list
        for box in boxes:
            boxes_list.append(int(box))
        
        for i in range(len(boxes_list)):
            for j in range(len(boxes_list)):
                if i != j:
                    if boxes_list[j] == 1:
                        answer[i]+=abs(j-i)
                        
        return answer