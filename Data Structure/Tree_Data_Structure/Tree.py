class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    if root is None:
        return Node(data)
    else:
        if data < root.data:
            root.left = insert(root.left, data)
        else:
            root.right = insert(root.right, data)
    return root

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.data)
        inorder_traversal(root.right)

# Daraxtni yaratish
root = None
root = insert(root, 5)
root = insert(root, 3)
root = insert(root, 8)
root = insert(root, 1)
root = insert(root, 4)

# Daraxtni o'qish
inorder_traversal(root)


# Natija
#      5
#    /   \
#   3     8
#  / \
# 1   4

# Inorder (Left, Root, Right)  1 3 4 5 8
# Postrder (Root, Left, Right) 3 1 4 5 8
# Preoder (Left, Right, Root) 1 4 3 8 5
