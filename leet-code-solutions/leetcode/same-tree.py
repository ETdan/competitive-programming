# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # print("///////////")
        # print(p)
        # print(q)

        if p != None and q != None:
            if p.val == q.val:
                left = True
                right = True
                if p.left or q.left:
                    left = self.isSameTree(p.left, q.left)

                if p.right or q.right:
                    right = self.isSameTree(p.right, q.right)
                if not (p.right or q.right) and not (p.left or q.left):
                    left = right =True

                return left and right

            else:
                return False
        else:
            # print("Here")
            return p == None and q == None

        # return True