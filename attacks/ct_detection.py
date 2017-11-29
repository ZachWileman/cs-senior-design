from scapy.all import *
'''
from scapy.arch.windows import compatibility
from scapy.all import log_runtime, MTU, ETH_P_ALL, PcapTimeoutElapsed, plist
compatibility.log_runtime = log_runtime
compatibility.MTU = MTU
compatibility.PcapTimeoutElapsed = PcapTimeoutElapsed
compatibility.ETH_P_ALL = ETH_P_ALL
compatibility.plist = plist
'''
global COUNTER
COUNTER = 0
BBB = "192.168.7.2"
'''
FIN = 0x01
SYN = 0x02
RST = 0x04
PSH = 0x08
ACK = 0x10
URG = 0x20
ECE = 0x40
CWR = 0x80
'''
packet = IP(dst=BBB)/TCP()
packet[TCP].flags = "UFP"

#Method 1
'''
F = packet['TCP'].flags    # this should give you an integer
if F & FIN:
	if F & URG:
		if F & PSH:
			print("ALERT")
'''
#Method 2
F = packet.sprintf('%IP.dst%')
packet.show()
print(F)
if F == "FPU":
	print("ALERT")


def pkt_callback(pkt):
    #print(COUNTER)
    #COUNTER = COUNTER + 1
    F = pkt.sprintf('%TCP.flags%')
    Dst = pkt.sprintf('%IP.dst%')
    Src = pkt.sprintf('%IP.src%')
    DPort = pkt.sprintf('%TCP.dport%')
    SPort = pkt.sprintf('%TCP.sport%')
    if F == "FPU":
    	print("ALERT")
    	print(Dst)
    	print(Src)
    	print(DPort)
	#print(SPort)

sniff( prn=pkt_callback, filter="tcp", store=0)

#sniff(prn = lambda F: F = packet.sprintf('%TCP.flags%') print(F) if F == "FPU": print("ALERT"), filter="tcp", store=0)

#a=sniff(count=50)
#a.show()

#packet.show()
