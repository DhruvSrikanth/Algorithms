# Time Complexity - O (h)

from bst_data_structure import Node

from bst_in_order_traversal import in_order_traversal

from bst_insert import insert

def search(root, num):
    if not root or root.val == num:
        return root
    elif root.val > num:
        return search(root.left, num)
    else:
        return search(root.right, num)

test = False
if test:
    root = Node(50)
    root = insert(root, 40)
    root = insert(root, 60)
    root = insert(root, 30)
    root = insert(root, 45)
    root = insert(root, 55)
    root = insert(root, 65)

    node_ = search(root, 45)
    print(node_.val)
