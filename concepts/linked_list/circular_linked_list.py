class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def display(self):
        temp = self.head
        while temp is not None:
            print(f"{temp.val} --> ", end="")
            temp = temp.next
            if temp == self.head:
                break
        print("END")

    def insert_first(self, val):
        node = Node(val)

        if self.head is None:
            self.head = node
            self.tail = node
            self.tail.next = self.head
            self.head.next = self.tail
            return

        self.tail.next = node
        node.next = self.head
        self.head = node

    def insert_last(self, val):
        node = Node(val)

        if self.tail is None:
            self.insert_first(val)
            return

        self.tail.next = node
        node.next = self.head
        self.tail = node

    def delete(self, val):
        if self.head is None:
            return

        if val == self.head.val:
            if self.head == self.tail:
                self.head = None
                self.tail = None
                return

            self.head = self.head.next
            self.tail.next = self.head
            return


        temp = self.head
        while temp is not None:
            if val == temp.next.val:
                temp.next = temp.next.next
                break
            temp = temp.next
            if temp == self.head:
                break


cll = CircularLinkedList()
cll.insert_first(6)
cll.insert_first(7)
cll.insert_first(8)
#
# cll.display()
#
cll.insert_last(27)
cll.display()

# cll.delete(27)
cll.display()


