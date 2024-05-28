# Problem: Maximum XOR of Two Numbers in an Array - https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(2)]

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,num):
        curr = self.root
        for i in range(32, -1, -1):
            val = 1 if (1 << i) & num else 0
            if curr.children[val] == None:
                curr.children[val] = TrieNode()
            curr = curr.children[val]

    def find_max(self, num):
        res = 0
        curr = self.root
        for i in range(32, -1, -1):
            val = 1 if (1 << i) & num else 0
            if val:
                if curr.children[0]:
                    res += 2 ** i
                    curr = curr.children[0]
                else:
                    curr = curr.children[1]
            else:
                if curr.children[1]:
                    res += 2 ** i
                    curr = curr.children[1]
                else:
                    curr = curr.children[0]
        return res

    def findMaximumXOR(self, nums: List[int]) -> int:
        maxVal = 0
        for num in nums:
            self.insert(num)
        for num in nums:
            maxVal = max(maxVal, self.find_max(num))
        return maxVal
        
