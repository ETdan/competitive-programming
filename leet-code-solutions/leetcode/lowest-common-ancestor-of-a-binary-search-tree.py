# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
        p_order = []
        q_order = []

        def searchBST(root, val, arr):
            if root:
                if val < root.val:
                    arr.append(root)
                    return searchBST(root.left, val, arr)
                elif val > root.val:
                    arr.append(root)
                    return searchBST(root.right, val, arr)
                else:
                    arr.append(root)
                    return arr

        p_order = set(searchBST(root, p.val, p_order))
        q_order = searchBST(root, q.val, q_order)

        for val in range(len(q_order)-1,-1,-1):
            if q_order[val] in p_order:
                return q_order[val]

