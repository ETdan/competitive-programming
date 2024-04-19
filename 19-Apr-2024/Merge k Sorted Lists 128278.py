# Problem: Merge k Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        idx = 0
        for index, LinkedList in enumerate(lists):
            if LinkedList:
                heap.append((LinkedList.val, idx, LinkedList))
                idx += 1

        heapq.heapify(heap)

        head = ListNode()
        dummy = ListNode()

        head.next = dummy

        while heap:
            node = heapq.heappop(heap)
            
            dummy.next = node[-1]
            dummy = dummy.next

            if node[-1].next:
                nextNode = node[-1].next
                heapq.heappush(heap,(nextNode.val, idx, nextNode))
                idx += 1
                
        return head.next.next
