import timeit
import yaml

from udp import answer


def to_yaml(arg):
    return yaml.dump(arg)

def from_yaml(arg):
    return yaml.load(arg, Loader=yaml.Loader)


time = timeit.default_timer()
serialized = to_yaml({"str": "a", "list": [1, 2, 3]})
serialization_time = timeit.default_timer() - time

time = timeit.default_timer()
deserialized = from_yaml(serialized)
deserialization_time = timeit.default_timer() - time

answer('yaml', f'yaml ser/deser time: {serialization_time}, {deserialization_time}\n')
