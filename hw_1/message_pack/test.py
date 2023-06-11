import msgpack
import timeit

from udp import answer

DATA = {"name": "Daniil", "surname": "Petraytis"}

def to_msg(arg):
    return msgpack.dumps(arg)

def from_msg(arg):
    return msgpack.loads(arg)


time = timeit.default_timer()
serialized = to_msg(DATA)
serialization_time = timeit.default_timer() - time

time = timeit.default_timer()
deserialized = from_msg(serialized)
deserialization_time = timeit.default_timer() - time

answer('message_pack', f'message_pack ser/deser time: {serialization_time}, {deserialization_time}\n')
