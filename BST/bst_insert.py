# Time Complexity - O (h)

from bst_data_structure import Node
from bst_in_order_traversal import in_order_traversal

def insert(root, num):
    if not root:
        return Node(num)
    else:
        if root.val == num:
            return root
        elif root.val > num:
            root.left = insert(root.left, num)
        else:
            root.right = insert(root.right, num)
    return root

test = False
if test:
    root = Node(50)
    root = insert(root, 40)
    root = insert(root, 60)
    root = insert(root, 30)
    root = insert(root, 45)
    root = insert(root, 55)
    root = insert(root, 65)

    in_order_traversal(root)



