import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
#conf.verb=0

# Set up target IP
ip = IP(dst="192.168.1.127")
SYN = ip / TCP(sport=RandNum(1024, 65535), dport=80, flags="S", seq=42)
# Send SYN and receive SYN,ACK
print(str(SYN['TCP'].flags))
while (1):
    SYNACK =sr1(SYN)#,inter=0.3,retry=2,timeout=4)
    print(str(SYNACK['TCP'].flags))
# Create ACK packet
#ACK = ip / TCP(sport=SYNACK.dport, dport=80, flags="A", seq=SYNACK.ack, ack=SYNACK.seq + 1)
# SEND our ACK packet
#send(ACK)
