# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []

        def helper(root, r, c):
            if root:
                if root.right and root.left:
                    left = helper(root.left, r + 1, c - 1)
                    right = helper(root.right, r + 1, c + 1)

                    answer.append([r, root.val])
                    # return [[c, root.val, r] + [left] + [right]]

                elif root.left:
                    left = helper(root.left, r + 1, c - 1)
                    answer.append([r, root.val])
                    # return [[c, root.val, r] + [left]]
                elif root.right:
                    right = helper(root.right, r + 1, c + 1)
                    answer.append([r, root.val])
                    # return [[c, root.val, r], right]
                else:
                    answer.append([r, root.val])

        helper(root, 0, 0)
        answer.sort(key=lambda x: x[0])
        if len(answer) == 0:
            return []

        max_col = answer[-1][0]
        length = max_col + 1

        ans = [[] for _ in range(length)]

        for r, val in answer:
            ans[r].append(val)
            
        for i in range(len(ans)):
            if i % 2 != 0:
                ans[i] = ans[i][::-1]
            
        return ans
