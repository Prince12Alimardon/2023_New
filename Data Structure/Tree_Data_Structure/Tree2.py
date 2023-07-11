class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preorder_traversal(root):
    if root:
        print(root.data)
        preorder_traversal(root.left)
        preorder_traversal(root.right)


def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.data)
        inorder_traversal(root.right)


def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.data)


# Daraxtni yaratish
root = Node(5)
root.left = Node(3)
root.right = Node(8)
root.left.left = Node(1)
root.left.right = Node(4)

# Daraxtni tarqatishlar
print("Preorder traversal:")
preorder_traversal(root)

print("Inorder traversal:")
inorder_traversal(root)

print("Postorder traversal:")
postorder_traversal(root)


# Preorder traversal:
# 5
# 3
# 1
# 4
# 8
# Inorder traversal:
# 1
# 3
# 4
# 5
# 8
# Postorder traversal:
# 1
# 4
# 3
# 8
# 5
