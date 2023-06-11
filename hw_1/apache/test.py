import timeit
import fastavro

from io import BytesIO
from udp import answer


class Helper:
    def __init__(self):
        self.s = "123"
        self.i = 123
        self.d = {
            "1" : 1,
            "2" : 2
        }

helper = Helper()


schema = {
    "namespace": "namespace.avro",
    "type": "record",
    "name": "schema",
    "fields": [
        {"name": "s", "type": "string"},
        {"name": "i", "type": "int"},
        {"name": "d", "type": {"type": "map", "values": "int"}}
    ]
}

def to_avro():
    bytes_writer = BytesIO()
    fastavro.schemaless_writer(bytes_writer, schema, helper.__dict__)
    return bytes_writer.getvalue()

def from_avro(arg):
    bytes_writer = BytesIO()
    bytes_writer.write(arg)
    bytes_writer.seek(0)
    fastavro.schemaless_reader(bytes_writer, schema)
    

time = timeit.default_timer()
serialized = to_avro()
serialization_time = timeit.default_timer() - time

time = timeit.default_timer()
deserialized = from_avro(serialized)
deserialization_time = timeit.default_timer() - time

answer('apache', f'apache ser/deser time: {serialization_time}, {deserialization_time}\n')
