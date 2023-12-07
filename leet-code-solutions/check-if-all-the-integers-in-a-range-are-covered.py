class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        left_to_right_list=[]
        ranges_interval_set=set()
        for i in range(left,right+1):
            left_to_right_list.append(i)
        
        for start,end in ranges:
            for i in range(start,end+1):
                ranges_interval_set.add(i)
        
        
        for i in left_to_right_list:
            if i not in ranges_interval_set:
                return False
            
        return True