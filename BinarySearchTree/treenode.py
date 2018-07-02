from .entry import Entry
from .const import (NULL_NODE_ADDRESS, INT_BYTE_SIZE, NODE_BYTE_SIZE)
from .serializers import IntSerializer


class TreeNode(object):

    def __init__(self, key:int = 0, left_node_address: int = NULL_NODE_ADDRESS, right_node_address:int = NULL_NODE_ADDRESS):
        self.entry = Entry(key)
        self.left_node_address = left_node_address
        self.right_node_address = right_node_address

    def dump(self) -> bytes:
        data = (
            self.entry.dump() +
            IntSerializer.serializer(self.left_node_address) +
            IntSerializer.serializer(self.right_node_address)
        )
        return data

    def load(self, data: bytes):
        assert len(data) == NODE_BYTE_SIZE
        self.entry.load(data[0 : INT_BYTE_SIZE])
        self.left_node_address = IntSerializer.deserialize(data[INT_BYTE_SIZE : 2 * INT_BYTE_SIZE])
        self.right_node_address = IntSerializer.deserialize(data[2 * INT_BYTE_SIZE : ])

