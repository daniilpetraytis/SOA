import msgpack
import sys
import timeit

from udp import answer

DATA = {"name": "Daniil", "surname": "Petraytis"}

def to_msg(arg):
    return msgpack.dumps(arg)

def from_msg(arg):
    return msgpack.loads(arg)


time = timeit.default_timer()
serialized = to_msg(DATA)
size_of_data = sys.getsizeof(serialized)
ser_time = timeit.default_timer() - time

time = timeit.default_timer()
deserialized = from_msg(serialized)
deser_time = timeit.default_timer() - time

answer('message_pack', f'message_pack - {size_of_data} - {ser_time} ms - {deser_time} ms\n')
