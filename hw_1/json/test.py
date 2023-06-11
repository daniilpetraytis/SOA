import json
import sys
import timeit

from udp import answer

JSON_DATA = {"name": "Daniil", "surname": "Petraytis"}


time = timeit.default_timer()
serialized = json.dumps(JSON_DATA)
size_of_data = sys.getsizeof(serialized)
ser_time = timeit.default_timer() - time

time = timeit.default_timer()
deserialized = json.loads(serialized)
deser_time = timeit.default_timer() - time

answer('json', f'json - {size_of_data} - {ser_time} ms - {deser_time} ms\n')
