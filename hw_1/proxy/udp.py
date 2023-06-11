import os
import socket


PROXY_PORT = 2000
UNICAST_PORT = 1999
MULTICAST_PORT = 1998

formats = ["apache", "json", "message_pack", "xml", "yaml"]

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("proxy", PROXY_PORT))

while True:
    req, addr = sock.recvfrom(128)
    req = req.decode().split()

    if len(req) != 2 or req[0] != "get_result":
        sock.sendto(b'Request is not correct.\n', addr)
    
    else:
        if req[1] in formats:
            sock.sendto(b'get_result\n', (req[1], UNICAST_PORT))
        elif req[1] == "all":
            sock.sendto(b'get_result\n', (os.getenv("MULTICAST_GROUP", default="224.0.0.0"), MULTICAST_PORT))
        else:
            sock.sendto(b'Incorrect format received.\n', addr)

        if req[1] == "all":
            for _ in range(len(formats)):
                answer, _ = sock.recvfrom(128)
                sock.sendto(answer, addr)
        else:
            answer, _ = sock.recvfrom(128)
            sock.sendto(answer, addr)
