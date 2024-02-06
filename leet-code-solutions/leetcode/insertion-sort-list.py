# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return 

        tempArr = []
        temp = head
        while temp is not None:
            tempArr.append(temp.val)
            temp = temp.next

        i = 0
        tempArr.sort()
        temp = head
        while temp is not None:
            temp.val = tempArr[i]
            i = i + 1
            temp = temp.next

        return head
        




        