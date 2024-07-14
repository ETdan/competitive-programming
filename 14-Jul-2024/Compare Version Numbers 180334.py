# Problem: Compare Version Numbers - https://leetcode.com/problems/compare-version-numbers/

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split('.')
        version2 = version2.split('.')
        
        i = 0
        j = 0
        
        while i < len(version1) and j < len(version2):
            if int(version1[i]) > int(version2[j]):
                return 1
            elif int(version1[i]) < int(version2[j]):
                return -1

            i += 1
            j += 1
    
        if len(version1) < len(version2):
            for i in range(i,len(version2)):
                if int(version2[i]) !=0:
                    return -1
            else:
                return 0
        elif len(version1) > len(version2):
            for i in range(i,len(version1)):
                if int(version1[i]) !=0:
                    return 1
            else:
                return 0
        else:
            return 0
