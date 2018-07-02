# On-Disk-Binary-Search-Tree-For-Fun
An on-disk binary search tree for fun.


Bplustree
=========

An on-disk Binary Search tree for Python 3.

It feels like a dict, but stored on disk. When to use it?

This project is under development: the format of the file may change between
versions. Do not use as your primary source of data.



Concurrency(To Be Done)
-----------

The tree is thread-safe, it follows the multiple readers/single writer pattern.

It is safe to:

- Share an instance of a ``BPlusTree`` between multiple threads

It is NOT safe to:

- Share an instance of a ``BPlusTree`` between multiple processes
- Create multiple instances of ``BPlusTree`` pointing to the same file

