class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        Dict={}
        i=0
        for o in order:
            Dict[o]=i
            i+=1
        
        for i in range(len(words)-1):
            if Dict[words[i][0]] > Dict[words[i+1][0]]:
                    return False
            elif Dict[words[i][0]] == Dict[words[i+1][0]]:
                length = min(len(words[i]),len(words[i+1]))
                for j in range(length):
                    if Dict[words[i][j]] < Dict[words[i+1][j]]:
                        break
                    
                    if Dict[words[i][j]] > Dict[words[i+1][j]]:
                        # print(words[i][j],words[i+1][j])
                        return False
                else:
                    if len(words[i]) > len(words[i+1]):
                        return False
        return True