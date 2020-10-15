class Node():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList():
    def __init__(self, head=None):
        self.head = head
    
    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count 

    def print(self):
        head = self.head
        while head:
            print(head.data, end=" ")
            head = head.next

    def search(self, data):
        head = self.head
        while head:
            if head.data == data:
                return True
            head = head.next
        return False
    
    def delete(self, data):
        current = self.head
        prev = current.next
        while current:
            # prev can be null here 
            if current.data == data:
                break 
            prev = current 
            current = current.next
        if prev:
            prev.next = current.next
        else:
            self.head = current.next

l = LinkedList()
l.insert(1)
l.insert(2)
l.insert(3)

l.print()
print("")
print(l.size())
print(l.search(2))
print(l.search(5))
print(l.delete(2))
l.print()