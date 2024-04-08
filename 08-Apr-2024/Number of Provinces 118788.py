# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

# class Solution:
#     def findCircleNum(self, isConnected: List[List[int]]) -> int:
#         adjecency_list=defaultdict(set)

#         # make an adjecency list

#         for i in range(len(isConnected)):
#             for j in range(len(isConnected[0])):
#                 # adjecency_list[isConnected[j]]

#         # loop through the list and delete
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # // building our root list
        l1 = [0]*len(isConnected[0])
        for i in range(len(l1)):
            l1[i] = i
        
        # // returns root of existing vertex
        def get_root(x):
            return l1[x]
        
        # // update root of existing index
        def union(x,y):
            Rx = get_root(x)
            Ry = get_root(y)

            if(Rx != Ry):
                for i in range(0,len(l1)):
                    if l1[i] == Ry:
                        l1[i] = Rx

        # // traversing only the upper traingular matrix to save time
        for i in range(0,len(isConnected)):
            for j in range(i+1,len(isConnected[0])):
                if isConnected[i][j] == 1:
                    union(i,j)
            
        return len(set(l1))