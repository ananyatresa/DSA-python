class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        temp = self.head
        while temp is not None:
            print(f"{temp.val} --> ", end="")
            temp = temp.next
        print("END")

    def insert_last(self, list_nodes):
        if self.head is None:
            self.head = list_nodes[0]
        temp = self.head
        for i in range(1, len(list_nodes)):
            temp.next = list_nodes[i]
            temp = temp.next


    def check_for_cycle(self, head):
        fast = head
        slow = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False

    def length_of_cycle(self, head):
        fast = head
        slow = head
        c=0
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                temp = slow.next
                c=1
                while fast != temp:
                    c+=1
                    temp = temp.next
        return c


ll1 = LinkedList()
cyclic_node = ListNode(1)
list_of_nodes = [ListNode(3),ListNode(2), cyclic_node, ListNode(0), cyclic_node, ListNode(4)]

ll1.insert_last(list_of_nodes)
ll1.display()




