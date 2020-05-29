# STACK 

# This is my implementation for a stack (LIFO)

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        return self.items
    
    def pop(self):
        result = None
        if self.size() == 0:
            print("Error: the stack is empty, unable to pop item from the stack")    
        else:
            result = self.items.pop()
        return result

    def popAll(self):
        if self.size() == 0:
            print("Error: the stack is empty, unable to pop items from the stack")
        else: 
            while not self.isEmpty():
                print("Removing {} from stack...".format(self.pop()), end=" ")
                print("Done.")
        print()

    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)

    def display(self):
        if self.isEmpty():
            print("The stack is empty use the 'push' method to add an item")
        elif self.size() == 1:
            print("The stack has {} item".format(self.size()))
            print("|_{}_| (next and last item)".format(self.items[0]))
        else:
            print("The stack has {} items".format(self.size()))
            for i, item in enumerate(self.items[::-1]):
                printStr = "| {} | ".format(item)
                if i == 0:
                    printStr += "(next item)"
                elif i == len(self.items) -1:
                    printStr = "|_{}_| (last item)".format(item)
                print(printStr)

s = Stack()

s.display()
print("\nAdding 3 to the stack...")
s.push(3)
s.display()
print("\nAdding 2 to the stack...")
s.push(2)
s.display()
print("\nAdding 1 to the stack...")
s.push(1)
s.display()
print("\nAdding 4 to the stack...")
s.push(4)
s.display()
print("\nRemoving next item from the stack...")
s.pop()
s.display()
print("\nRemoving all items from the stack...")
s.popAll()
s.display()
print()