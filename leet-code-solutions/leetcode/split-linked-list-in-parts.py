# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        answer=[]
        nums=[0]*k

        length=0
        temp=head

        while temp:
            length+=1
            temp=temp.next
        
        i=0
        while length:
           nums[i%k]+=1
           length-=1 
           i+=1

        temp=head

        for i,num in enumerate(nums):
            headi=ListNode(0)
            tempi=headi
            while num:
                num-=1
                tempi.next=temp
                temp=temp.next
                tempi=tempi.next
            tempi.next=None
            answer.append(headi.next)

        return answer