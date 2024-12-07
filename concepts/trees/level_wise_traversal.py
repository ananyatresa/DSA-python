# BFS
import queue
from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.height = 0


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def get_height(self, node):
        if node is None:
            return -1
        return node.height

    def display_nodes(self, node, indent):
        if node is None:
            return

        print(f"{indent}{node.val}")
        self.display_nodes(node.left, indent + "\t")
        self.display_nodes(node.right, indent + "\t")


    def display(self):
        self.display_nodes(self.root, "")


    def insert(self):
        val = int(input("Enter root node: "))
        self.root = Node(val)
        self.insert_nodes(self.root)

    def insert_nodes(self, node):
        left = bool(input(f"Do you want to insert left of {node.val}? "))
        if left:
            val = int(input("Enter val: "))
            node.left = Node(val)
            self.insert_nodes(node.left)

        right = bool(input(f"Do you want to insert right of {node.val}? "))
        if right:
            val = int(input("Enter val: "))
            node.right = Node(val)
            self.insert_nodes(node.right)

        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1

    # level order traversal
    def bfs(self, root):
        if root is None:
            return []

        outer_list = []
        my_q = queue.Queue()
        my_q.put(root)

        while not my_q.empty():
            curr_level_size = my_q.qsize()
            curr_level_list = []
            for i in range(curr_level_size):
                node = my_q.get()
                curr_level_list.append(node.val)
                if node.left:
                    my_q.put(node.left)
                if node.right:
                    my_q.put(node.right)

            outer_list.append(curr_level_list)

        return outer_list


    # find average of nodes on each level and return as an array
    def find_level_average(self, root):
        if not root:
            return []

        outer_list = []
        que = queue.Queue()
        que.put(root)

        while not que.empty():
            level_size = que.qsize()
            total_sum = 0
            for i in range(level_size):
                node = que.get()
                total_sum +=node.val
                if node.left:
                    que.put(node.left)
                if node.right:
                    que.put(node.right)
            avg = total_sum/level_size
            outer_list.append(avg)
        return outer_list

    # find level order succesor of a node in binary tree
    def find_node_successor(self, root, key):
        if not root:
            return None

        my_q = queue.Queue()
        my_q.put(root)

        while not my_q.empty():
            node = my_q.get()
            if node.left:
                my_q.put(node.left)
            if node.right:
                my_q.put(node.right)
            if node.val == key:
                break
        return my_q.get()

    # zigzag level order traversal -using bfs and deque to support normal and reverse order
    def zigzag(self, root):
        if root is None:
            return []

        outer_list = []
        my_q = deque()
        my_q.append(root)
        normal = True

        while len(my_q):
            curr_level_size = len(my_q)
            curr_level_list = []
            if normal:
                # normal order-remove from front(left) and add in back(right)
                for i in range(curr_level_size):
                    node = my_q.popleft()
                    curr_level_list.append(node.val)
                    if node.left:
                        my_q.append(node.left)
                    if node.right:
                        my_q.append(node.right)
            else:
                # reverse order-remove from back(right) and add in front(left)
                for i in range(curr_level_size):
                    node = my_q.pop()
                    curr_level_list.append(node.val)
                    if node.right:
                        my_q.appendleft(node.right)
                    if node.left:
                        my_q.appendleft(node.left)
            normal = not normal

            outer_list.append(curr_level_list)

        return outer_list

    # move right pointers
    def level_wise_right_pointers(self, root):
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












bt = BinaryTree()
bt.insert()
bt.display()
