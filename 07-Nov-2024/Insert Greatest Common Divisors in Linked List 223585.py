# Problem: Insert Greatest Common Divisors in Linked List - https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        ans = ListNode()  
        cur = ans  
        
        while head.next:
            gcd_val = math.gcd(head.val, head.next.val)  
            
            cur.next = ListNode(head.val)  
            cur.next.next = ListNode(gcd_val)  
            
            head = head.next  
            cur = cur.next.next  

        cur.next = ListNode(head.val)  
        
        return ans.next  