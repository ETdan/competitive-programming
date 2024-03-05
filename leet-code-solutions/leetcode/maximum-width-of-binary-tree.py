# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        level_width = defaultdict(list)

        def backTrack(root, level, width):
            if not root:
                return

            level_width[level].append(width)

            backTrack(root.left, level + 1, width * 2 + 1)
            backTrack(root.right, level + 1, width * 2 + 2)

        backTrack(root, 0, 0)

        max_width = float("-inf")

        for key, val in level_width.items():
            max_width = max(max(val) - min(val) + 1, max_width)

        return max_width
