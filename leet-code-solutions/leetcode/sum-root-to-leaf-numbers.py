# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        tot_sum=0
        def helper(root,curr):
            nonlocal tot_sum
            if root:
                if root.left and root.right:
                    helper(root.left,(root.val + curr)*10)
                    helper(root.right,(root.val + curr)*10)
                elif root.left:
                    helper(root.left,(root.val + curr)*10)
                elif root.right:
                    helper(root.right,(root.val + curr)*10)
                else:
                    tot_sum+=(curr + root.val)
                    
        helper(root,0)
        return tot_sum