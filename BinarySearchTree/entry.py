from .const import (ENDIAN, INT_BYTE_SIZE)
from .serializers import IntSerializer


class Entry(object):
    def __init__(self, key: int):
        self.key = key

    def dump(self) -> bytes:
        return IntSerializer.serializer(self.key)



    def load(self, data: bytes):
        self.key = IntSerializer.deserialize(data)


    def __lt__(self, other):
        return self.key < other.key

    def __eq__(self, other):
        return self.key == other.key

    def __gt__(self, other):
        return self.key > other.key

    def __ge__(self, other):
        return self.key >= other.key

    def __le__(self, other):
        return self.key <= other.key


