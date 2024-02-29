# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        val = 0
        def helper(root):
            nonlocal val,k
            if root.left:
                helper(root.left)
            k-=1
            # print(root.val)
            if k == 0:
                val = root.val

            if root.right:
                helper(root.right)
                
        helper(root)

        return val