# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        answer=head
        temp=head

        while temp:
            while temp and temp.val == answer.val:
                temp=temp.next
            answer.next=temp
            answer=answer.next

        
        return head