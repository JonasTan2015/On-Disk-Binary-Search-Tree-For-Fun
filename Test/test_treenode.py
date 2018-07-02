import unittest

from BinarySearchTree.treenode import TreeNode

class TestTreeNodeMethods(unittest.TestCase):

    def test_load_and_dump(self):
        treenode = TreeNode(1, 2, 3)
        serialized_data = treenode.dump()
        treenode.load(serialized_data)
        self.assertEqual(treenode.entry.key, 1)
        self.assertEqual(treenode.left_node_address, 2)
        self.assertEqual(treenode.right_node_address, 3)

