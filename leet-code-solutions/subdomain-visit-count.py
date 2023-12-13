class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        Dict=defaultdict(int)
        answer=[]

        for subdomain in cpdomains:
            visit,domain = subdomain.split(" ")
            domain=domain.split(".")[::-1]
            preve=""
            for i in range(0,len(domain)):
                if preve == "":
                    preve+=domain[i]
                else:
                    preve = domain[i] + "." + preve
                
                Dict[preve]+=int(visit)

        for key, value in Dict.items():
            answer.append(str(value) + " " + str(key))

        return answer