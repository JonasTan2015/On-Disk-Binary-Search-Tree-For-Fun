import unittest
import os

from BinarySearchTree.tree import Tree


class TestTree(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestTree, self).__init__(*args, **kwargs)
        currdir = os.path.dirname(os.path.realpath(__file__))
        self.path = os.path.join(currdir, 'test_data')
        self.tree = Tree(self.path)

    def test_insert(self):
        for i in [3, 1, 2, 5, 4]:
            self.tree.insert(i)
        traverse_order = self.tree.traverse()
        for i in [1,2,3,4,5]:
            self.assertEqual(i, traverse_order[i - 1])

    def cleanup(self):
        self.tree.close()


class TestLoadTree(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestLoadTree, self).__init__(*args, **kwargs)
        currdir = os.path.dirname(os.path.realpath(__file__))
        self.path = os.path.join(currdir, 'test_data')
        self.tree = Tree(self.path)

    def test_traverse(self):
        traverse_order = self.tree.traverse()
        for i in [1,2,3,4,5]:
            self.assertEqual(i, traverse_order[i - 1])

    def cleanup(self):
        try:
            os.remove(self.path)
        except OSError:
            pass