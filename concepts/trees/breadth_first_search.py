import queue
from collections import deque
from queue import Queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def insert(self):
        val = int(input("Enter root node: "))
        self.root = TreeNode(val)
        self.insert_val(self.root)

    def insert_val(self, node):

        left = input("Do you want to insert left? ")
        if left == 'y':
            val = int(input("Enter val: "))
            node.left = TreeNode(val)
            node.left = self.insert_val(node.left)

        right = input("Do you want to insert right? ")
        if right == 'y':
            val = int(input("Enter val: "))
            node.right = TreeNode(val)
            node.right = self.insert_val(node.right)

        return node

    def display(self):
        self.display_vals(self.root, "")

    def display_vals(self, node, indent):
        if node is None:
            return
        print(f"{indent}{node.val}")

        # print left
        self.display_vals(node.left, indent + "\t")
        # print right
        self.display_vals(node.right, indent + "\t")

    def bfs(self, root):
        outer_list = []
        if root is None:
            return outer_list

        que = Queue()
        que.put(root)

        while not que.empty():
            level_size = que.qsize()
            level_list = []
            for _ in range(level_size):
                node = que.get()
                level_list.append(node.val)

                if node.left:
                    que.put(node.left)
                if node.right:
                    que.put(node.right)

            outer_list.append(level_list)
        return outer_list

    def level_order_successor(self, root, target):
        if root is None:
            return None

        que = Queue()
        que.put(root)

        while not que.empty():
            node = que.get()
            if node.val == target:
                break
            if node.left:
                que.put(node.left)
            if node.right:
                que.put(node.right)

        return que.get()

    def zigzg_traversal(self, root):
        outer_list = []
        if root is None:
            return outer_list

        dque = deque()
        dque.append(root)
        normal_order = True

        while len(dque) != 0:
            level_size = len(dque)
            level_list = []
            if normal_order:
                # normal - pop from LHS and push in RHS (leftnode, rightnode)
                for _ in range(level_size):
                    node = dque.popleft()
                    level_list.append(node.val)

                    if node.left:
                        dque.append(node.left)
                    if node.right:
                        dque.append(node.right)
            else:
                # reverse - pop from RHS and push in LHS (rightnode, leftnode)
                for _ in range(level_size):
                    node = dque.pop()
                    level_list.append(node.val)

                    if node.right:
                        dque.appendleft(node.right)
                    if node.left:
                        dque.appendleft(node.left)
            normal_order = not normal_order
            outer_list.append(level_list)
        return outer_list

    # O(n) SC
    def right_next_pointers(self, root):
        if root is None:
            return None

        que = queue.Queue()
        que.put(root)

        while not que.empty():
            node = que.get()
            if node.left:
                node.left.next = node.right
                que.put(node.left)
            if node.right:
                que.put(node.right)
                if node.next:
                    node.right.next = node.next.left

        return root

    # O(1) SC
    def right_next_pointers_without_queue(self, root):
        if root is None:
            return None

        leftmost = root
        while leftmost.left:
            curr = leftmost
            while curr:
                curr.left.next = curr.right
                if curr.next:
                    curr.right.next = curr.next.left
                curr = curr.next
            leftmost = leftmost.left

        return root


    def right_side_view(self, root):
        outer_list = []
        if root is None:
            return outer_list

        que = Queue()
        que.put(root)

        while not que.empty():
            level_size = que.qsize()
            node = None
            for _ in range(level_size):
                node = que.get()
                if node.left:
                    que.put(node.left)
                if node.right:
                    que.put(node.right)

            outer_list.append(node.val)
        return outer_list


bt = BinaryTree()
bt.insert()
bt.display()
