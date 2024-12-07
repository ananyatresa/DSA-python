class Node:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def display(self):
        temp = self.head
        while temp is not None:
            print(f"{temp.val}  --> ", end="")
            temp = temp.next
        print("END")

    def display_reverse(self):
        temp = self.tail
        while temp is not None:
            print(f"{temp.val}  --> ", end="")
            temp = temp.prev
        print("START")

    def find(self, val):
        temp = self.head
        while temp is not None:
            if val == temp.val:
                return temp
            temp = temp.next
        return None

    def insert_first(self, val):
        node = Node(val)
        if self.head is None:
            self.head = node
            self.tail = node
            return
        node.next = self.head
        self.head.prev = node
        self.head = node
        self.size+=1

    def insert_last(self, val):
        node = Node(val)

        if self.tail is None:
            self.insert_first(val)
            return

        node.prev = self.tail
        self.tail.next = node
        self.tail = node
        self.size += 1


    def insert_after(self, prev_val, new_val):
        p = self.find(prev_val)

        if p.next is None:
            self.insert_last(new_val)
            return

        node = Node(new_val)
        node.prev = p
        node.next = p.next
        p.next.prev = node
        p.next = node

        self.size += 1

    def delete_first(self):
        if self.size == 0:
            return
        self.head = self.head.next
        self.head.prev = None
        if self.head is None:
            self.tail = None

        self.size -= 1

    def delete_last(self):
        if self.size <= 1:
            self.delete_first()
            return
        self.tail = self.tail.prev
        self.tail.next = None
        self.size -= 1

    def delete(self, val):
        if self.head.val == val:
            self.delete_first()
            return
        if self.tail.val == val:
            self.delete_last()
            return
        node = self.find(val)

        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

        self.size -= 1






DLL = DoublyLinkedList()
DLL.insert_first(3)
DLL.insert_first(22)
DLL.insert_first(31)
DLL.insert_first(56)
DLL.display()
DLL.insert_last(49)
DLL.display()

DLL.insert_after(56, 99)
DLL.display()

DLL.delete_first()
DLL.display()


DLL.delete_last()
DLL.display()

DLL.delete(22)
DLL.display()

DLL.display_reverse()




