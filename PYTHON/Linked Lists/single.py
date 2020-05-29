class Node: 
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Single:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head

    def display(self):
        self._display(self.head)
        print()
    
    def _display(self, node):
        if node is self.tail:
            print(node.data, end="")
            return
        else: 
            print("{} -> ".format(node.data), end="")
            self._display(node.next)

    def size(self):
        counter = 1
        return self._size(self.head, counter)

    def _size(self, node, counter):
        if node.next is None:
            return counter
        else: 
            return 1 + self._size(node.next, counter)

    def add(self, data):
        return self._add(self.head, data)

    def _add(self, node, data, success=False):
        if node.next is None: 
            node.next = Node(data)
            self.tail = node.next
            return True
        else:
            return success or self._add(node.next, data)

print("Creating a list with one node...")
l = Single(5)
l.display()
print("Size: {} \n".format(l.size()))
print("Adding 3 to the list...")
l.add(3)
l.display()
print("Size: {} \n".format(l.size()))

print("Adding 2 to the list...")
l.add(2)
l.display()
print("Size: {} \n".format(l.size()))

print("Adding 1 to the list...")
l.add(1)
l.display()
print("Size: {} \n".format(l.size()))