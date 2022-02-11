# Time Complexity - O (h)

from bst_data_structure import Node

from bst_insert import insert

def min_value_node(root):
    if root.left == None:
        return root
    else:
        return min_value_node(root.left)

test = False
if test:
    root = Node(50)
    root = insert(root, 40)
    root = insert(root, 60)
    root = insert(root, 30)
    root = insert(root, 45)
    root = insert(root, 55)
    root = insert(root, 65)

    min_value_node_ = min_value_node(root)
    print(min_value_node_.val)
