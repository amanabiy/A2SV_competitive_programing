class Node:
   def __init__(self, dataval=None):
      self.val = dataval
      self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size or index < 0:
            return -1
        count = 1
        temp = self.head
        while count <= index:
            temp = temp.next
            count += 1
        return temp.val if temp else -1
        
    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            count = 1
            temp = self.head
            while count < index and temp:
                temp = temp.next
                count += 1
            new_node = Node(val)
            new_node.next = temp.next
            temp.next = new_node
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        temp = self.head
        while count < index - 1:
            temp = temp.next
            count += 1
        temp.next = temp.next.next if temp.next else None



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
