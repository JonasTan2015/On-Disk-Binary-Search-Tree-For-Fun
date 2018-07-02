from .const import(ENDIAN, INT_BYTE_SIZE)

class IntSerializer(object):
    @staticmethod
    def serializer(data: int) -> bytes :
        return data.to_bytes(INT_BYTE_SIZE, ENDIAN)

    @staticmethod
    def deserialize(data: bytes)-> int:
        assert len(data) == INT_BYTE_SIZE
        return int.from_bytes(data, ENDIAN)