import sys
import timeit

from udp import answer

from xml_marshaller import xml_marshaller


def to_xml(arg):
    return xml_marshaller.dumps(arg)

def from_xml(arg):
    return xml_marshaller.loads(arg)


time = timeit.default_timer()
serialized = to_xml({"1": "a", "2": "b"})
size_of_data = sys.getsizeof(serialized)
ser_time = timeit.default_timer() - time

time = timeit.default_timer()
deserialized = from_xml(serialized)
deser_time = timeit.default_timer() - time

answer('xml', f'xml - {size_of_data} - {ser_time} ms - {deser_time} ms\n')
