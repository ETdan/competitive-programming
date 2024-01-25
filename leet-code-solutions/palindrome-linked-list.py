# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head) -> Optional[ListNode]:
        # print(head,"head")
        prev = None
        cur = head
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        
        return prev
     


    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp=head
        counter=0

        while temp:
            temp=temp.next
            counter+=1
        
        if counter == 1:
            return True

        counter=(counter+1)//2

        after_mid_ptr=head
        before_mid_ptr=head

        for i in range(counter):
            after_mid_ptr=after_mid_ptr.next

        # reverse
        after_mid_ptr=self.reverseList(after_mid_ptr)

        # print(before_mid_ptr,"//",after_mid_ptr,counter)

        # for i in range(counter):
        #     # print(before_mid_ptr.val,after_mid_ptr.val)
        #     if before_mid_ptr.val!=after_mid_ptr.val:
        #         return False
        #     after_mid_ptr=after_mid_ptr.next
        #     before_mid_ptr=before_mid_ptr.next

        while before_mid_ptr and after_mid_ptr:
            if before_mid_ptr.val!=after_mid_ptr.val:
                return False
            after_mid_ptr=after_mid_ptr.next
            before_mid_ptr=before_mid_ptr.next
            
        return True