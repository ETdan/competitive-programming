# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def merge(r1,r2):
            if r1 and r2:
                new_node = TreeNode(r1.val + r2.val)
                if r1.left and r2.left:
                    new_node.left = merge(r1.left,r2.left)
                else:
                    new_node.left = r1.left or r2.left

                if r1.right and r2.right:
                    new_node.right = merge(r1.right,r2.right)
                else:
                    new_node.right = r1.right or r2.right
                return new_node
            else:
                return r1 or r2

        return merge(root1,root2)