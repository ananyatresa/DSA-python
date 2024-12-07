from concepts.LinkedList.linked_list import LinkedList

# leetcode solution node wise
def mergeTwoLists(self, head1, head2):
    new_head = None
    new_tail = new_head
    while head1 is not None and head2 is not None:
        if head1.val < head2.val:
            new_tail.next = head1
            head1 = head1.next
        else:
            new_tail.next = head2
            head2 = head2.next
        new_tail = new_tail.next

    new_tail.next = head1 if head1 is not None else head2
    return new_head.next

# persoanl solution ll wise
# def merge(head1, head2):
#     ll3 = LinkedList()
#     while head1 is not None and head2 is not None:
#         if head1.val < head2.val:
#             ll3.insert_last(head1.val)
#             head1 = head1.next
#         else:
#             ll3.insert_last(head2.val)
#             head2 = head2.next
#
#     while head1 is not None:
#         ll3.insert_last(head1.val)
#         head1 = head1.next
#     while head2 is not None:
#         ll3.insert_last(head2.val)
#         head2 = head2.next
#     ll3.display()






ll1 = LinkedList()
ll1.insert_last(1)
ll1.insert_last(2)
ll1.insert_last(3)

ll2 = LinkedList()
ll2.insert_last(1)
ll2.insert_last(2)
ll2.insert_last(4)
# ll1.display()

merge(ll1.head, ll2.head)

# print(ll.head.value)
# print(ll.tail.value)
# print(ll.ret_list())