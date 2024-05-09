# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class Solution:
    parent = []
    size = []

    def constract(self, size):
        self.parent = [i for i in range(size)]
        self.size = [1] * size

    def union(self, x, y):
        # print(x,y)
        parentx = self.find(x)
        parenty = self.find(y)

        if parentx != parenty:
            if self.size[parentx] > self.size[parenty]:
                self.parent[parenty] = self.parent[parentx]
                self.size[parentx] += self.size[parenty]
            else:
                self.size[parenty] += self.size[parentx]
                self.parent[parentx] = self.parent[parenty]

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def isConnected(self, x, y):
        return self.find(x) == self.find(y)

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        self.constract(len(accounts))

        pre_answer = [[] for i in range(len(accounts))]

        for i in range(len(accounts)):
            temp = set(accounts[i][1:])
            accounts[i] = [accounts[i][0]]
            accounts[i].append(temp)

        # union all the accounts that have the one or more similar accounts  
        # print(self.parent)
        for _ in range(5):
            for i in range(len(accounts)):
                for j in range(i+1,len(accounts)):
                    for account in accounts[i][1]:
                        # print(account,accounts[j][1])
                        if account in accounts[j][1]:
                            self.union(i,j)
                        

        
        # print(self.parent)

        for i in range(len(self.parent)):
            if pre_answer[self.parent[i]]:
                pre_answer[self.parent[i]][1].update(accounts[i][1])
            else:
                pre_answer[self.parent[i]].extend(accounts[i])

        answer=[]
        for i in range(len(pre_answer)):
            if pre_answer[i]:
                answer.append([pre_answer[i][0]])
                answer[-1].extend(sorted(list(pre_answer[i][1])))

        return answer
