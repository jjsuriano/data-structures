from node import Node
import math

class BinaryTree:
    def __init__(self, node: Node):
        self.root = node

# add a node to the tree
    def add(self, current: Node, data: int):
        if current is None:
            return Node(data, 2)
        
        if data < current.data:
            current.children[0] = self.add(current.children[0], data)
        elif data > current.data:
            current.children[1] = self.add(current.children[1], data)
        else: 
            print("Unable to add node to the tree\n")
        return current
    
# display the tree
# like this, 50 is the root node: 
#                 100
#         75
#                 65
# 50
#         25
#                 0
    def display(self, root: Node, level=0):
        if root is None:
            return
        else:
            level += 1
            self.display(root.children[1], level)
            print(("\t"*level) + str(root.data))
            print()
            self.display(root.children[0], level)
            

# determine the total number of levels the tree has
    def levels(self, root: Node, level=0):
        if root is None:
            return level
        else:
            level += 1
            left = self.levels(root.children[0], level)
            right = self.levels(root.children[1], level)
        return max(left, right)