# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left=[]
        right=[]

        def traverseLeft(root):
            if root:
                left.append(root.val)
                traverseLeft(root.left)
                traverseLeft(root.right)
            else:
                left.append(None)


        def traverseRight(root):
            if root:
                right.append(root.val)
                traverseRight(root.right)
                traverseRight(root.left)
            else:
                right.append(None)
        
        traverseLeft(root.left)
        traverseRight(root.right)

        # print(left)
        # print(right)

        return left == right