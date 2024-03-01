# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            if root:
                if root.right and root.left:
                    left = helper(root.left)
                    right = helper(root.right)
                    # print(root.val, left , right,"/////////////////")

                    Lmin_=min(left[2],left[1])
                    Lmax_=max(left[2],left[1])
                    Lmaxv=max(abs(root.val - Lmin_),abs(root.val - Lmax_))
                    
                    Rmin_=min(right[2],right[1])
                    Rmax_=max(right[2],right[1])
                    Rmaxv=max(abs(root.val - Rmin_),abs(root.val - Rmax_))
                    # print(Lmin_,Rmin_,Lmax_,Rmax_)
                    # print(max(Lmaxv,Rmaxv,left[0],right[0]),min(Rmin_,root.val,Lmin_),max(Rmax_,root.val,Lmax_),"rrrrrrrrrrrrlllllllllll")
                    
                    return [max(Lmaxv,Rmaxv,left[0],right[0]),min(Rmin_,root.val,Lmin_),max(Rmax_,root.val,Lmax_)]
                elif root.left:
                    left = helper(root.left)

                    min_=min(left[2],left[1])
                    max_=max(left[2],left[1])
                    maxv=max(abs(root.val - min_),abs(root.val - max_))

                    # print(max(maxv,left[0]),min(min_,root.val),max(max_,root.val),"llllllllllllll")

                    return [max(maxv,left[0]),min(min_,root.val),max(max_,root.val)]
                elif root.right:

                    right = helper(root.right)

                    min_=min(right[2],right[1])
                    max_=max(right[2],right[1])
                    maxv=max(abs(root.val - min_),abs(root.val - max_))
                    
                    # print(max(maxv,right[0]),min(min_,root.val),max(max_,root.val),"rrrrrrrrrrrrrrrrrrrrrrr")
                    return [max(maxv,right[0]),min(min_,root.val),max(max_,root.val)]
                else:
                    # print("heeeeeeeeeeeeeeeeeeeer")
                    return [0,root.val,root.val]

        return helper(root)[0]