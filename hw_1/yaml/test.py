import sys
import timeit
import yaml

from udp import answer


def to_yaml(arg):
    return yaml.dump(arg)

def from_yaml(arg):
    return yaml.load(arg, Loader=yaml.Loader)


time = timeit.default_timer()
serialized = to_yaml({"str": "a", "list": [1, 2, 3]})
size_of_data = sys.getsizeof(serialized)
ser_time = timeit.default_timer() - time

time = timeit.default_timer()
deserialized = from_yaml(serialized)
deser_time = timeit.default_timer() - time

answer('yaml', f'yaml - {size_of_data} - {ser_time} ms - {deser_time} ms\n')
