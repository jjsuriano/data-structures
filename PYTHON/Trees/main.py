from binary import BinaryTree

def main():
    tree = BinaryTree(5)
    print(tree)
    tree + 3
    print(tree)
    tree + 7
    print(tree)
    tree + 1
    print(tree)
    print(repr(tree))

if __name__ == "__main__":
    main()