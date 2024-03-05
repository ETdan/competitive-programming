# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def dvideAndConcur(left,right):
            if left > right:
                return

            if left == right:
                return TreeNode(nums[left])

            mid = (right+left)//2

            root = TreeNode(nums[mid])

            root.left = dvideAndConcur(left,mid-1)
            root.right = dvideAndConcur(mid+1,right)

            return root

        return dvideAndConcur(0,len(nums)-1)