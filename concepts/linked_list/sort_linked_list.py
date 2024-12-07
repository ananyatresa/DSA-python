# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def find_mid(self, head):
        fast = head
        slow = head
        prev = slow
        while fast is not None and fast.next is not None:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        # break the list
        if prev is not None:
            prev.next = None
        return slow

    def merge(self, head1, head2):
        new_head = ListNode(0)
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

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # applying merge sort

        # Base case: if no elements or only 1 elem in LL, its already sorted, so returns head
        if head is None or head.next is None:
            return head

        # find mid
        mid = self.find_mid(head)
        left_node = self.sortList(head)
        right_node = self.sortList(mid)

        return self.merge(left_node, right_node)
