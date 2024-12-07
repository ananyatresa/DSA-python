from concepts.LinkedList.linked_list import LinkedList


def remove_duplicate_nodes(node):
    if node is None or node.next is None:
        return node

    if node.value == node.next.value:
        node.next = node.next.next
        remove_duplicate_nodes(node)
    else:
        remove_duplicate_nodes(node.next)

    return node




ll = LinkedList()
ll.insert_first(3)
ll.insert_first(3)
ll.insert_first(3)
ll.insert_first(2)
ll.insert_first(1)
ll.insert_first(1)
ll.display()
remove_duplicate_nodes(ll.head)
# print(ll.head.value)
# print(ll.tail.value)
print(ll.ret_list())