# Problem: All Nodes Distance K in Binary Tree - https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if k ==0:
            return [target.val]

        adj_list=defaultdict(set)

        q=deque()
        q.append(root)

        while q:
            node = q.popleft()

            if node.left:
                q.append(node.left)
                
                adj_list[node.left.val].add(node.val)
                adj_list[node.val].add(node.left.val)

            if node.right:
                q.append(node.right)
                
                adj_list[node.right.val].add(node.val)
                adj_list[node.val].add(node.right.val)
        
        
        visited=set()
        
        q.append(target.val)
        visited.add(target.val)

        while q:
            k-=1

            for _ in range(len(q)):
                node = q.popleft()
                for neighbour in adj_list[node]:
                    if neighbour not in visited:
                        q.append(neighbour)
                        visited.add(neighbour)

            if k < 1:
                return list(q)

        return list(q)