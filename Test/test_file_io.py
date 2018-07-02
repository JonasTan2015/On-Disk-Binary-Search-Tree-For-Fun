import unittest
from BinarySearchTree.file_io import (open_file, read_from_file, write_to_file)
import os

class TestFileIO(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestFileIO, self).__init__(*args, **kwargs)
        currdir = os.path.dirname(os.path.realpath(__file__))
        self.file = open_file(os.path.join(currdir, 'test_data'))


    def test1(self):
        data = 123
        data_bytes = data.to_bytes(4, 'little')
        write_to_file(self.file, data_bytes)
        read_bytes = read_from_file(self.file, 0, len(data_bytes))
        read_int = int.from_bytes(read_bytes, 'little')
        self.assertEqual(read_int, data)


    # Test whether data written in file can be read afterwards
    def continual_write(self):
        for i in range(5):
            data = i.to_bytes(4, 'little')
            write_to_file(self.file, data, i * 4)

        for i in range(5):
            data = read_from_file(self.file, 0*i, 0*i + 4)
            read_int = int.from_bytes(data, 'little')
            self.assertEqual(read_int, i)

    # Close the test data file
    def cleanup(self):
        self.file.close()
