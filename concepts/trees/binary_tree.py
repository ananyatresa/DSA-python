class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def display(self):
        self.display_nodes(self.root, "")

    def display_nodes(self, node, indent):
        if node is None:
            return
        # print current node
        print(f"{indent}{node.val}")
        # call left node
        self.display_nodes(node.left, indent + "\t")
        # call right node
        self.display_nodes(node.right, indent + "\t")

    def populate_nodes(self, node):
        # insert left
        left = bool(input(f"Do you want to add left of {node.val} ?"))
        if left:
            val = int(input(f"Enter the value you want to add left of {node.val} : "))
            node.left = Node(val)
            self.populate_nodes(node.left)

        # insert right
        right = bool(input(f"Do you want to add right of {node.val} ?"))
        if right:
            val = int(input(f"Enter the value you want to add right of {node.val} : "))
            node.right = Node(val)
            self.populate_nodes(node.right)

    def populate(self):
        # insert root
        val = int(input(f"Enter the root node: "))
        root = Node(val)
        self.root = root
        self.populate_nodes(self.root)

    #  TC = O(n) and SC=O(n) , Used in BST
    def inorder_traversal(self, node):
        # LNR
        result = []

        def inorder(node):
            if node is None:
                return []

            inorder(node.left)
            result.append(node.val)
            inorder(node.right)

        inorder(node)
        return result

    #  TC = O(n) and SC=O(n)
    def preorderTraversal(self, node):
        # NLR
        result = []

        def preorder(node):
            if node is None:
                return []

            result.append(node.val)
            preorder(node.left)
            preorder(node.right)

        preorder(node)
        return result



bt = BinaryTree()
# bt.populate()
bt.root = Node(2)
bt.root.left = Node(3)
bt.root.right = Node(1)
bt.root.left.left = Node(4)
bt.display()
print(bt.inorder_traversal(bt.root))
