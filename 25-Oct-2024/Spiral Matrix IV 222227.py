# Problem: Spiral Matrix IV - https://leetcode.com/problems/spiral-matrix-iv/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        mat=[[-1]*n for _ in range(m)]
        left=0
        right=n
        top=0
        bottom=m

        while left < right and top < bottom:
            # left to right
            for i in range(left,right):
                if head.val != -1:
                    mat[top][i]=head.val
                if head.next:
                    head=head.next
                else:
                    head.val=-1

            top+=1

            # top to bottom right col
            for i in range(top,bottom):
                if head.val != -1:
                    mat[i][right-1]=head.val
                if head.next:
                    head=head.next
                else:
                    head.val=-1

            right-=1

            # we don't need to always go in the 4 directions
            # the minimum moves are left to right and top to bottom once
            if not (left < right and top < bottom):
                break

            # right to left bottom row
            for i in range(right-1,left-1,-1):
                if head.val != -1:
                    mat[bottom-1][i]=head.val
                if head.next:
                    head=head.next
                else:
                    head.val=-1

            bottom-=1

            # # bottom to top left col
            for i in range(bottom-1,top-1,-1):
                if head.val != -1:
                    mat[i][left]=head.val
                if head.next:
                    head=head.next
                else:
                    head.val=-1

            left+=1
        return mat