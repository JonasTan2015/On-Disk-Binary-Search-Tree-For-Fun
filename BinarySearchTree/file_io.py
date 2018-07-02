
import io
import os

class ReachEndOfFile(Exception):
    """Read a file until its end"""

# create a file if not exists.
# Return a IO.FileIO object
def open_file(path: str) -> io.FileIO:
    if not os.path.exists(path):
        file = open(path, mode='x+b', buffering=0)
    else:
        file = open(path, mode='r+b', buffering = 0)
    return file


# Given a range of offset
# Retrieve bytes from the file
def read_from_file(file: io.FileIO, start: int, stop: int)-> bytes:
    assert stop > start
    file.seek(start)
    data = bytes()
    while file.tell() < stop:
        read_data = file.read(stop - file.tell())
        if read_data == b'':
            raise ReachEndOfFile('Read until the end of file')
        data += read_data
    assert len(data) == stop - start
    return data

# Given a starting position of file {@code start}
# Write the bytes into file
def write_to_file(file: io.FileIO, data: bytes, start: int=0):
    length_to_write = len(data)
    file.seek(start)
    written = 0
    while written < length_to_write:
        written += file.write(data[written:])
    os.fsync(file.fileno())


from .treenode import TreeNode
from .const import (NODE_BYTE_SIZE)

class FileManager(object):
    def __init__(self, path: str):
        self._file = open_file(path)
        self._fileno = self._file.fileno()

    def close(self):
        self._file.close()

    # Retrieve a treenode at position {@code start} from file
    def read_node(self, start:int) -> TreeNode:
        data = read_from_file(self._file, start=start, stop= start + NODE_BYTE_SIZE)
        node = TreeNode()
        node.load(data)
        return node

    # Write tree node into file from offset {@code start}
    def write_node(self, node: TreeNode, start: int):
        data = node.dump()
        write_to_file(self._file, data, start)

    # Return size of binary tree file so that Tree class could determine how many nodes are inserted already.
    def size(self):
        return os.fstat(self._fileno).st_size