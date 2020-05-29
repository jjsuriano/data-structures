# QUEUE

# This is my implementation for a queue (FIFO)

class Queue: 
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)
        return self.items
    
    def pop(self):
        value = None
        if self.size() == 0:
            print("Error: the queue is empty, unable to pop item from the queue")    
        else:
            value = self.items[0]
            del self.items[0]
        return value

    def popAll(self):
        if self.size() == 0:
            print("Error: the queue is empty, unable to pop items from the queue")
        else: 
            while not self.isEmpty():
                print("Removing {} from queue...".format(self.pop()), end=" ")
                print("Done.")
        print()

    def display(self):
        if self.isEmpty():
            print("The queue is empty use the 'push' method to add an item")
        elif self.size() == 1:
            print("The queue has {} item".format(self.size()))
            print("| {} | (next and last item)".format(self.items[0]))
        else:
            print("The queue has {} items".format(self.size()))
            for i, item in enumerate(self.items):
                printStr = "| {} | ".format(item)
                if i == 0:
                    printStr += "(next item)"
                elif i == len(self.items) -1:
                    printStr += "(last item)"
                print(printStr)

q = Queue()

q.display()
print("\nAdding 3 to the queue...")
q.push(3)
q.display()
print("\nAdding 2 to the queue...")
q.push(2)
q.display()
print("\nAdding 1 to the queue...")
q.push(1)
q.display()
print("\nAdding 4 to the queue...")
q.push(4)
q.display()
print("\nRemoving next item from the queue...")
q.pop()
q.display()
print("\nRemoving all items from the queue...")
q.popAll()
q.display()
print()