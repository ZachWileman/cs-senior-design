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

BBB = "192.168.1.127"
FIN = 0x01
SYN = 0x02
RST = 0x04
PSH = 0x08
ACK = 0x10
URG = 0x20
ECE = 0x40
CWR = 0x80

#Start addition
counter = 0
numPackets = 0
#End addition

packet = IP(dst=BBB)/TCP()
packet[TCP].flags = "UFP"

#Method 1
F = packet['TCP'].flags    # this should give you an integer
if F & FIN:
    if F & URG:
        if F & PSH:
            print("ALERT")

#Method 2
F = packet.sprintf('%TCP.flags%')
print(F)
if F == "FPU":
    print("ALERT")


def pkt_callback(pkt):
    global numPackets
    global counter
    F = pkt.sprintf('%TCP.flags%')
    #print(F)
    if F == "FPU":
        print("ALERT")
    #Start addition
    numPackets += 1
    if F == "SA": #Might need to be S.
        counter += 1
        if counter >= 50:
            print("ALERT SYN FLOOD")
    if (numPackets % 100) == 0: #After 100 packets are parsed, subtract 10 off counter to prevent errant tripping of alarm
        counter -= 10
    #End addition

sniff( prn=pkt_callback, filter="tcp", store=0)

#sniff(prn = lambda F: F = packet.sprintf('%TCP.flags%') print(F) if F == "FPU": print("ALERT"), filter="tcp", store=0)

#a=sniff(count=50)
#a.show()

#packet.show()
