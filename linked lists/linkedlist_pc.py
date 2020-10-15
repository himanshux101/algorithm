class Node:
    def __init__(self, value):
        self.next = None
        self.value = value

class List:
    def __init__(self, value):
        self.head = Node(value)

    def insert(self, value):
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node(value)

    def find(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            else:
                current = current.next
        return False

    def delete(self, value):
        if self.find(value) is not True:
            return "not in list"
        else:
            current = self.head
            while current is not None:
                if current.next.value == value:
                    current.next = current.next.next
                    break
                else:
                    current = current.next

    def print(self):
        current = self.head
        while current is not None:
            if current.value is not None:
                print(current.value, end=" ")
            current = current.next
        print("")

    def reverse_iterative(self):
        prev = None
        cur = self.head
        next = cur

        while cur != None:
            next = next.next
            cur.next = prev 
            prev = cur 
            cur = next
        self.head = prev

    def reverse_recur(self, head):
        if head is None:
            return head
        rev = self.reverse_recur(head.next)
        head.next.next = head
        head.next = null
        return head

    def insertion_sort(self, head):
        dummy_head = Node(0)
        dummy_head.next = node_to_insert = head 

        while head and head.next:
            if head.value > head.next.value:
                node_to_insert = head.next 
                node_to_insert_pre = dummy_head
                
                while node_to_insert_pre.next.value < node_to_insert.value:
                    node_to_insert_pre = node_to_insert_pre.next

                head.next = node_to_insert.next 
                node_to_insert.next = node_to_insert_pre.next 
                node_to_insert_pre.next = node_to_insert
            else:
                head = head.next
        return dummy_head.next

v = List(None)

v.insert(10)
v.insert(40)
v.insert(30)
v.insert(90)
v.print()
print('---')
head = v.head.next
v.head = v.insertion_sort(head)
v.print()