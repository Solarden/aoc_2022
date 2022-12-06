from input import datastream


class DatastreamResolver:
    def __init__(self, datastream: str):
        self.datastream = datastream

    def get_index_of_first_marker(self, datastream_length: int) -> int:
        index: int = 0
        for index, character in enumerate(self.datastream):
            datastream_packet: str = self.datastream[index:index + datastream_length]
            if len(set(datastream_packet)) == len(datastream_packet) == datastream_length:
                index = index + datastream_length
                break
        return index


if __name__ == "__main__":
    resolver = DatastreamResolver(datastream=datastream)
    print(resolver.get_index_of_first_marker(4))
    print(resolver.get_index_of_first_marker(14))
