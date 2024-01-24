# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head

        if head.next == None:
            return head

        curr = head
        prev = curr

        curr=curr.next
        prev.next=None

        while curr:
            next = None
            if curr.next:
                next = curr.next

            curr.next = prev

            if next == None:
                return curr

            prev =curr
            curr = next
            # print(prev.val," ",curr.val,next.val)

        return curr
