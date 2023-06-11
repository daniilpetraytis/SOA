import json
import timeit

from udp import answer

JSON_DATA = {"name": "Daniil", "surname": "Petraytis"}


time = timeit.default_timer()
serialized = json.dumps(JSON_DATA)
ser_time = timeit.default_timer() - time

time = timeit.default_timer()
deserialized = json.loads(serialized)
deser_time = timeit.default_timer() - time

answer('json', f'json ser/deser time: {ser_time}, {deser_time}\n')
