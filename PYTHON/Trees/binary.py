import math

class Node:
    def __init__(self, item=None):
        self.data = item
        self.left = self.right = None


class BinaryTree:
    def __init__(self, item):
        self.root = Node(item)

# add a node to the tree
    def __add__(self, item):
        self._insert(self.root, item)

    def _insert(self, current: Node, data: int):
        if current is None:
            return Node(data)
        
        if data < current.data:
            current.left = self._insert(current.left, data)
        elif data > current.data:
            current.right = self._insert(current.right, data)
        else: 
            print("Unable to insert, value already in the tree")
        return current
    
# display the tree
# like this, 50 is the root node: 
#                 100
#         75
#                 65
# 50
#         25
#                 0
# inorder traversal starting on the right side (right, root, left)
    
    def __str__(self):
        height = len(self)
        display = "BinaryTree has " +  str(height) + " levels." + "\n" if height != 1 else "BinaryTree has " +  str(height) + " level." + "\n"
        return display + self._display(self.root)

    def _display(self, root: Node, level=0, result=""):
        if root is None:
            return ""
        result = self._display(root.right, level+1, result) + "\t"*level + str(root.data) + '\n' + self._display(root.left, level+1, result)
        return result

    def __repr__(self):
        return f"BinaryTree({self._inorder(self.root)})"

    def _inorder(self, root: Node, items=[]):
        if root is None:
            return
        self._inorder(root.left, items)
        items.append(root.data)
        self._inorder(root.right, items)
        return items

# determine the total number of levels the tree has
# a tree's height
    def __len__(self):
        return self._height(self.root)

    def _height(self, root: Node):
        if root is None:
            return 0
        return 1 + max(self._height(root.left), self._height(root.right))