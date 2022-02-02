# Time complexity of - O (h), h is the height of the tree
# We are assuming that the pointer manipulation is in constant time and it is

class Node:
    def __init__(self, val):
        self.data = val
        self.Leftchild = self.Rightchild = None


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, root, val):
    if root is None:
        return Node(val)

    else:
        if root.data <= val:
            root.Rightchild = self.insert(root.Rightchild, val)
        else:
            root.Leftchild = self.insert(root.Leftchild, val)

        return root

    if __name__ == '__main__':
    tree = Tree()
    for i in range(10):
        tree.insert(random.randint(0,100))
