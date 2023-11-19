class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        n = len(s)
        m = len(p)
        answer = []
        temp = deque(s[:m-1])

        dict = {}
        dict1={}
        for letter in p:
            if letter in dict:
                dict[letter] += 1
            else:
                dict[letter] = 1
        
        for letter in temp:
            if letter in dict1:
                dict1[letter] += 1
            else:
                dict1[letter] = 1

        for i in range(0,n-m+1):
            temp.append(s[i+m-1])
            # print(temp)

            if temp[-1] in dict1:
                dict1[temp[-1]] += 1
            else:
                dict1[temp[-1]] = 1

            
            if dict1 == dict:
                answer.append(i)
            
            # print(dict1,dict)
            
            t = temp.popleft()

            if dict1[t] == 1:
                dict1.pop(t)
            else:
                dict1[t]-=1


        return answer
