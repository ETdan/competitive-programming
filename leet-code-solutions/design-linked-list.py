class Node:
    def __init__(self,value=0):
        self.value=value
        self.next=None

class MyLinkedList:

    def __init__(self):
        self.size=0
        self.head=Node()       

    def get(self, index: int) -> int:
        currNode = self.head.next
        if index == 0:
            if currNode:
                return currNode.value
            else:
                return -1
        for i in range(index):
            if currNode.next:
                currNode=currNode.next
            else:
                return -1

        if currNode:
            return currNode.value

        return -1

    def addAtHead(self, val: int) -> None:
        n = Node(val)
        n.next=self.head.next
        self.head.next=n
        self.size+=1
        # print(self.head.value,"ah")

    def addAtTail(self, val: int) -> None:
        self.size+=1
        currNode = self.head.next
        if currNode:
            while currNode.next:
                currNode=currNode.next

            currNode.next=Node(val)
            # print(currNode.next.value,"at")
        else:
            n=Node(val)
            self.head.next=n

    def addAtIndex(self, index: int, val: int) -> None:
        currNode = self.head.next

        if self.size < index:
            return
        self.size+=1
        if currNode == None:
            n=Node(val)
            n.next=self.head.next
            self.head.next=n
        else:
            
            if index==0:
                n=Node(val)
                n.next=self.head.next
                self.head.next=n

            for i in range(index-1):
                if currNode.next:
                    currNode=currNode.next
                else:
                    break
            else:
                n=Node(val)
                if currNode.next:
                    n.next=currNode.next
                currNode.next=n

    def deleteAtIndex(self, index: int) -> None:
        currNode = self.head.next
        
        if index==0:
            if self.head.next:
                self.head.next=self.head.next.next
                self.size-=1

        for i in range(index-1):
            if currNode.next:
                currNode=currNode.next
            else:
                break
        else:
            if currNode.next:
                currNode.next=currNode.next.next
                self.size-=1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)