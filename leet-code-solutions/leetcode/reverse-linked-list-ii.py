# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        slow = head
        new_head = ListNode(None, None)
        new_head.next = head
        left_edge = ListNode(None, None)
        left_head = ListNode(None, None)
        prev = ListNode(None, None)
        trans = ListNode(None, None)
        
        if head.next is None or left == right:
            return head

        if left == 1:
            slow = new_head
            left_edge = slow
            for i in range(left-1):
                left_edge = slow
                slow=slow.next
            slow=slow.next
            left_head = slow
            
            trans=slow.next
            while (right-left):
                prev = slow
                slow = trans
                trans = slow.next
                slow.next = prev
                right-=1
            
            left_edge.next=slow
            left_head.next=trans

            return new_head.next

        left_edge = slow
        for i in range(left-2):
            slow=slow.next
            left_edge = slow
        slow=slow.next
        left_head = slow
        
        trans=slow.next
        while (right-left):
            prev = slow
            slow = trans
            trans = slow.next
            slow.next = prev
            right-=1
        
        left_edge.next=slow
        left_head.next=trans

        return head
