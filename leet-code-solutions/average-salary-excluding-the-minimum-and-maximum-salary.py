class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        min_sal=salary[0]
        max_sal=salary[0]
        sum=0
        for s in salary:
            if min_sal >s:
                min_sal=s
            if max_sal < s:
                max_sal=s
            sum+=s
        # print(min_sal,max_sal)
        return float((sum-min_sal-max_sal))/(len(salary)-2)