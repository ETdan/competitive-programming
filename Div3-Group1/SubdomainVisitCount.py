class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        dict={}

        for a in cpdomains:
            a=a.split(' ')
            count=int(a[0])
            site=str((a[1]))

            if site in dict:
                dict[site]+=count
            else:
                dict[site]=count

            site=site.split('.')

            if len(site) == 2:
                if site[1] in dict:
                    dict[site[1]]+=count
                else:
                    dict[site[1]]=count
            else:
                if site[1] + '.' + site[2] in dict:
                    dict[site[1] + '.' + site[2]]+=count
                else:
                    dict[site[1] + '.' + site[2]]=count
                if site[2] in dict:
                    dict[site[2]]+=count
                else:
                    dict[site[2]]=count

        li=[]
        for key,val in dict.items():
            con=str(val) + ' ' + key
            li.append(con)
        
        return li
