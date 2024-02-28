# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    max_dup=0
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        duplicate_counter=defaultdict(int)

        def traverse(root):
            if root:
                duplicate_counter[root.val]+=1
                self.max_dup=max(duplicate_counter[root.val],self.max_dup)
                traverse(root.left)
                traverse(root.right)
            return 

        traverse(root)

        answer = []
        for key,val in duplicate_counter.items():
            if val == self.max_dup:
                answer.append(key)
                
        return answer
        