import os
import select
import socket
import struct


PROXY_PORT = 2000
UNICAST_PORT = 1999
MULTICAST_PORT = 1998

MULTICAST_GROUP = os.getenv("MULTICAST_GROUP", default="224.0.0.0")
formats = ["apache", "json", "message_pack", "xml", "yaml"]


def answer(format_name: str, answer: str):
    multicast = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    multicast.bind((MULTICAST_GROUP, MULTICAST_PORT))
    mreq = struct.pack("=4sl", socket.inet_aton(MULTICAST_GROUP), socket.INADDR_ANY)
    multicast.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
    
    unicast = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    unicast.bind((format_name, UNICAST_PORT))

    while True:
        for curr_s in select.select([unicast, multicast], [], [])[0]:
            curr_s.recvfrom(128)
            curr_s.sendto(answer.encode(), ("proxy", PROXY_PORT))
