import unittest
from BinarySearchTree.entry import Entry



class TestEntryMethods(unittest.TestCase):

    def test_entry_dump_and_load(self):
        entry = Entry(15)
        data = entry.dump()
        entry.load(data)
        self.assertEqual(entry.key, 15)





