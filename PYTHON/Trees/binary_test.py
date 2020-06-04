import unittest
from binary import BinaryTree

class BinaryTreeTest(unittest.TestCase):
    def test_init(self):
        result = BinaryTree(5)
        self.assertEqual(len(result), 1)
        self.assertEqual(result.root.data, 5)
        self.assertEqual(result.root.left, None)
        self.assertEqual(result.root.right, None)
    
    def test_add(self):
        result = BinaryTree(5)
        result + 3
        self.assertEqual(len(result), 2)
        