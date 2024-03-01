# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []

        def helper(root, r, c):
            if root:
                if root.right and root.left:
                    left = helper(root.left, r + 1, c - 1)
                    right = helper(root.right, r + 1, c + 1)

                    answer.append([c,r, root.val])
                    # return [[c, root.val, r] + [left] + [right]]

                elif root.left:
                    left = helper(root.left, r + 1, c - 1)
                    answer.append([c,r, root.val])
                    # return [[c, root.val, r] + [left]]
                elif root.right:
                    right = helper(root.right, r + 1, c + 1)
                    answer.append([c,r, root.val])
                    # return [[c, root.val, r], right]
                else:
                    answer.append([c,r, root.val])

        helper(root, 0, 0)
        answer.sort(key=lambda x: (x[0], x[1],x[2]))
        min_col = answer[0][0]
        max_col = answer[-1][0]
        length = max_col - min_col + 1

        ans = [[] for _ in range(length)]
        for col,r,val in answer:
            ans[col+abs(min_col)].append(val)

        return ans
