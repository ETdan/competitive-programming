# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast=head
        slow=head

        while fast:
            if fast.next:
                fast=fast.next
            else:
                break

                
            if fast.next:
                fast=fast.next
            else:
                break

            slow=slow.next
            if slow == fast:
                return True
                
        return False