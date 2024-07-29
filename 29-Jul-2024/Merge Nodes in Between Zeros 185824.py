# Problem: Merge Nodes in Between Zeros - https://leetcode.com/problems/merge-nodes-in-between-zeros

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp_head=head

        while temp_head.next:
            temp=temp_head.next
            
            while temp.val !=0:
                temp_head.val+=temp.val
                temp=temp.next
            
            if temp.next:
                temp_head.next=temp
                temp_head=temp_head.next
            else:
                temp_head.next= None

        return head