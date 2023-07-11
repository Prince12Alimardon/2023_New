class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Ikkilik daraxtni yaratish
def create_binary_tree():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    return root

# Ikkilik daraxtni inorder tartibida tarqatish
def inorder_traversal(node):
    if node is not None:
        inorder_traversal(node.left)
        print(node.data)
        inorder_traversal(node.right)

# Ikkilik daraxtni preorder tartibida tarqatish
def preorder_traversal(node):
    if node is not None:
        print(node.data)
        preorder_traversal(node.left)
        preorder_traversal(node.right)

# Ikkilik daraxtni postorder tartibida tarqatish
def postorder_traversal(node):
    if node is not None:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.data)

# Ikkilik daraxtni yaratish va tarqatish
binary_tree = create_binary_tree()

print("Inorder traversal:")
inorder_traversal(binary_tree)

print("Preorder traversal:")
preorder_traversal(binary_tree)

print("Postorder traversal:")
postorder_traversal(binary_tree)


# Inorder traversal:
# 4
# 2
# 5
# 1
# 3
# Preorder traversal:
# 1
# 2
# 4
# 5
# 3
# Postorder traversal:
# 4
# 5
# 2
# 3
# 1
