# Using Recursion
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, node: Optional[ListNode]) -> Optional[ListNode]:
        if node is None or node.next is None:
            return node

        new_head = self.reverseList(node.next)
        new_head.next = node
        node.next = None

        return node

    def display(self, head):
        temp = head
        while temp is not None:
            print(f"{temp} --> ")
            temp = temp.next
        print("END")

sol = Solution()
sol.display()



