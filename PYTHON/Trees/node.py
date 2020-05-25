class Node:
    def __init__(self, data, numOfChildren=0):
        self.data = data
        self.children = []
        for i in range(0, numOfChildren):
            self.children.append(None)
    

# returns the number of children the Node has
    def numOfChildren(self):
        return len(self.children)

# remove a child
# if index is not given, it will delete the last child
# if index is given, it will try to remove child at index i
    def removeChild(self, index=None):
        size = self.numOfChildren()
        if index is None:
            i = size-1
        else: 
            i = index
        
        try:
            del self.children[i]
        except IndexError:
            print("Error: invalid index {}".format(i))

# prints the information of the Node
    def info(self):
        print("data: {}".format(self.data))
        print("children: {}".format(self.children))
