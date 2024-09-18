# Problem: Middle of the Linked List - https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head.next
        counter=0

        while slow != fast and fast:
            if fast:
                fast=fast.next
                counter+=1
            else:
                break

            slow=slow.next
            if fast:
                fast=fast.next
                counter+=1
            else:
                break
        # print(counter)
        # if counter % 2 ==0:
        #     slow = slow.next
        
        return slow