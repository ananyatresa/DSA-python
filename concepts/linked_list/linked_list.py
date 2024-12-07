class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedList:
    head = Node
    tail = Node
    size = 0

    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    # def ret_list(self):
    #     result = []
    #     temp = self.head
    #     while temp is not None:
    #         result.append(temp.val)
    #         temp = temp.next
    #     return result

    def display(self):
        temp = self.head
        while temp is not None:
            print(f"{temp.val} --> ", end="")
            temp = temp.next
        print("END")

    def insert_first(self, val):
        # create new node with val
        new_node = Node(val)

        # Point new node to current head
        new_node.next = self.head

        # Assign head as new Node
        self.head = new_node

        if self.tail is None:
            self.tail = self.head

        self.size += 1

    def insert_last(self, val):
        new_node = Node(val)

        if self.size == 0:
            self.insert_first(val)
            return

        # Point current tail to new node
        self.tail.next = new_node

        # Make new node as tail
        self.tail = new_node

        self.size += 1

    def get(self, index):
        temp = self.head
        for curr_idx in range(index):
            temp = temp.next

        return temp

    def insert_at(self, val, index):
        if index == 0:
            self.insert_first(val)
            return
        if index == self.size:
            self.insert_last(val)
            return

        # fetch previous node
        prev_node = self.get(index - 1)

        # create new node
        new_node = Node(val, prev_node.next)

        # Point prev_node to new_node
        prev_node.next = new_node

        self.size += 1

    def delete_first(self):
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.size -= 1

    def delete_last(self):
        if self.size <= 1:
            self.delete_first()
            return
        second_last_node = self.get(self.size - 2)
        self.tail = second_last_node
        self.tail.next = None

        self.size -= 1

    def delete_at(self, index):
        if index == 0:
            self.delete_first()
            return
        if index == self.size - 1:
            self.delete_last()
            return

        prev_node = self.get(index -1)

        # point prev_node to the to_be_deleted_node's next
        prev_node.next = prev_node.next.next

        self.size -= 1

    def insert_recur(self, val, index, node):
        if index == 0:
            new_node = Node(val)
            new_node.next = node
            return new_node

        node.next = self.insert_recur(val, index-1, node.next)
        return node

    def insert_recursion(self, val, index):
        self.head = self.insert_recur(val, index, self.head)

    def remove_duplicate_nodes(self, node):
        if node is None or node.next is None:
            return node

        if node.val == node.next.val:
            node.next = node.next.next
            self.size-=1
            self.remove_duplicate_nodes(node)
        else:
            self.remove_duplicate_nodes(node.next)

        return node

    def merge(self, ll1, ll2):
        head1 = ll1.head
        head2 =ll2.head
        ll3 = LinkedList()
        while head1 is not None and head2 is not None:
            if head1.val < head2.val:
                ll3.insert_last(head1.val)
                head1 = head1.next
            else:
                ll3.insert_last(head2.val)
                head2 = head2.next

        while head1 is not None:
            ll3.insert_last(head1.val)
            head1 = head1.next
        while head2 is not None:
            ll3.insert_last(head2.val)
            head2 = head2.next
        return ll3

    def middleNode(self, head):
        fast = head
        slow = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow

    def reverseList_recursion(self, node):
        if node is None or node.next is None:
            return node

        new_head = self.reverseList_recursion(node.next)
        new_head.next = node
        node.next = None

        return node

    def reverseList_iteratively(self, node):
        prev = None
        curr = node
        nex = curr.next
        while curr is not None:
            curr.next = prev
            prev = curr
            curr = nex
            if nex is not None:
                nex = nex.next
        prev = node




if __name__ == "__main__":
    ll1 = LinkedList()
    ll2 = LinkedList()
    ll1.insert_last(1)
    ll1.insert_last(2)
    ll1.insert_last(3)
    ll1.insert_last(4)
    ll1.display()

    # ll1.reverseList_recursion(ll1.head)
    ll1.reverseList_iteratively(ll1.head)
    ll1.display()

    # print(ll1.middleNode(ll1.head).val)





