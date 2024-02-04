# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return None
        
        second_head = ListNode()
        answer1 = second_head

        temp = head

        while temp:
            if temp.val < x:
                second_head.next= ListNode(temp.val)
                second_head = second_head.next
            temp = temp.next

        end_of_answer1=second_head
        end_of_answer1.next=None

        second_head = ListNode()
        answer2 = second_head
  
        temp = head

        while temp:
            if temp.val >= x:
                second_head.next= ListNode(temp.val)
                second_head = second_head.next
            temp = temp.next

        second_head.next=None

        end_of_answer1.next=answer2.next
        
        return answer1.next

