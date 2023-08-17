class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """

        dict={}
        for a in paths:
            a=a.split(' ')
            root=a[0]

            for files in range(1,len(a)):
                files=a[files].split('(')
                val=files[0]
                key=files[1]
                key=key[:-1]

                if key in dict:
                    value=dict[key]
                    value+=' ' +root +'/'+ val
                    dict[key]=value
                else:
                    dict[key]=root+'/'+ val

        answer=[]
        
        for key,val in dict.items():
            val=val.split(' ')
            a=[]
            if len(val) >1:
                answer.append(list(val))

        return answer
