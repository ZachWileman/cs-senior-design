import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
from random import randint

BBB = "192.168.1.127"
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
