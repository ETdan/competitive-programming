class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        
        dict={}
        for a in s1:
            if a in dict:
                dict[a]+=1
            else:
                dict[a]=1

        left=0
        right=len(s1)-1 
        # dict1={}
        status=True
        while right < len(s2):
            dict1=dict.copy()
            # print(dict1)
            for i in range(left,right+1):
                if s2[i] in dict1 and dict1[s2[i]] > 0:
                    dict1[s2[i]]-=1
                else:
                    status=False
                    break
            
            if status:
                for key,val in dict1.items():
                    if val != 0:
                        status = False
                        break
                if status:
                    return True
                else:
                    right+=1
                    left+=1
            else:
                    right+=1
                    left+=1

            status=True

        return False
