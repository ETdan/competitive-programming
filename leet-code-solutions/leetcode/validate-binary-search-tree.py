# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        valid = True

        def helper(root):
            nonlocal valid
            if root:
                if root.left and root.right:
                    left = helper(root.left)
                    right = helper(root.right)
                    # print(left,right,root.val)
                    if root.val <= max(left) or root.val >= min(right):
                        valid = False
                    return [
                        min([root.val] + left + right),
                        max([root.val] + left + right),
                    ]
                elif root.left:
                    left = helper(root.left)
                    if root.val <= max(left):
                        valid = False
                    return [min([root.val] + left), max([root.val] + left)]
                elif root.right:
                    right = helper(root.right)
                    if root.val >= min(right):
                        valid = False
                    return [min([root.val] + right), max([root.val] + right)]
                else:
                    return [root.val]

        helper(root)
        return valid
