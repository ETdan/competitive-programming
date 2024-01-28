# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        if not list2 and not list1:
            return list1
        
        head=ListNode()
        temp=head

        temp1=list1
        temp2=list2

        while temp1 and temp2:
            if temp1 and temp2: 
                if temp1.val <= temp2.val:
                    temp.next=temp1
                    temp = temp.next
                    temp1 = temp1.next
                else:
                    temp.next=temp2
                    temp = temp.next
                    temp2 = temp2.next
        
        while temp1:
            temp.next=temp1
            temp = temp.next
            temp1 = temp1.next

        while temp2:
            temp.next=temp2
            temp = temp.next
            temp2 = temp2.next
            
        return head.next
                
