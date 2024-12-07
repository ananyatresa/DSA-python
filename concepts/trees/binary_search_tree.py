class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.height = 0


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return -1
        return node.height

    def display_nodes(self, node, indent):
        if node is None:
            return None
        print(f"{indent}{node.val}")
        self.display_nodes(node.left, indent + "\t")
        self.display_nodes(node.right, indent + "\t")

    def display(self):
        self.display_nodes(self.root, "")

    def insert(self, val):
        self.root = self.insert_val(val, self.root)

    def insert_val(self, val, node):
        if node is None:
            new_node = Node(val)
            return new_node

        if val < node.val:
            new_node = self.insert_val(val, node.left)
            node.left = new_node

        if val > node.val:
            new_node = self.insert_val(val, node.right)
            node.right = new_node

        node.height = max(self.height(node.left), self.height(node.right)) + 1
        return node

    def check_balanced(self, node):
        if node is None:
            return True

        return abs(self.height(node.left)-self.height(node.right)) <= 1 and self.check_balanced(node.left) and self.check_balanced(node.right)

    def populate_sorted(self, nums, start, end):
        if start >= end:
            return
        mid = (start + end)//2
        self.insert(nums[mid])
        # LHS
        self.populate_sorted(nums, start, mid)
        # RHS
        self.populate_sorted(nums, mid+1, end)


    def populate_sorted_array(self, nums):
        self.populate_sorted(nums, 0, len(nums))


bst = BinarySearchTree()
bst.insert(15)
bst.insert(10)
bst.insert(20)
bst.insert(5)
# bst.insert(12)
# bst.insert(25)
# bst.insert(26)
# bst.display()
#
# print(bst.check_balanced(bst.root))

nums=[1,2,3,4,5,6]
bst.populate_sorted_array(nums)
bst.display()
