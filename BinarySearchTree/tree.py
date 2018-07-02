from typing import List

from .treenode import TreeNode
from .file_io import FileManager
from .const import (NULL_NODE_ADDRESS, NODE_BYTE_SIZE)

class Tree(object):
    def __init__(self, path: str):
        self._file_manager = FileManager(path)
        self.ROOTNODE_ADDR = 0
        self._size = self._file_manager.size() / NODE_BYTE_SIZE

    def insert(self, key: int):
        node = TreeNode(key)
        node_addr = self._size * NODE_BYTE_SIZE
        if self._size == 0:
            self._file_manager.write_node(node, 0)
            self._size += 1
            return

        curr_node = self._file_manager.read_node(0)
        curr_addr = 0
        while True:
            if curr_node.entry == node.entry:
                return
            elif curr_node.entry < node.entry:
                if curr_node.right_node_address != NULL_NODE_ADDRESS:
                    curr_addr = curr_node.right_node_address
                    curr_node = self._file_manager.read_node(curr_node.right_node_address)
                else:
                    self._file_manager.write_node(node, node_addr)
                    self._size += 1
                    curr_node.right_node_address = node_addr
                    self._file_manager.write_node(curr_node, curr_addr)
                    break
            else:
                if curr_node.left_node_address != NULL_NODE_ADDRESS:
                    curr_addr = curr_node.left_node_address
                    curr_node = self._file_manager.read_node(curr_node.left_node_address)
                else:
                    self._file_manager.write_node(node, node_addr)
                    self._size += 1
                    curr_node.left_node_address = node_addr
                    self._file_manager.write_node(curr_node, curr_addr)
                    break


    # Todo: implement iterator
    # Just for testing. Not a good way to recursively iterate the tree
    def traverse(self)-> List[int]:
        values = []
        if self._size == 0:
            return values

        root_node = self._file_manager.read_node(0)
        self._traverse(root_node, values)
        return values

    def _traverse(self, node: TreeNode, values:List[int]):
        if node.left_node_address != NULL_NODE_ADDRESS:
            left_node = self._file_manager.read_node(node.left_node_address)
            self._traverse(left_node, values)
        values.append(node.entry.key)
        if node.right_node_address != NULL_NODE_ADDRESS:
            right_node = self._file_manager.read_node(node.right_node_address)
            self._traverse(right_node, values)

    def close(self):
        self._file_manager.close()
        self._file_manager = None