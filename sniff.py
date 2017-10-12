#!/usr/bin/python3
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

#counter = 0

def sniff_packets(packet):
    #global counter
    #counter += 1
    # print('Packet #{}: {} ==> {}'.format(counter, packet[0][1].src, packet[0][1].dst))

    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst

        # you can filter with something like that
        if packet[IP].src == "192.168.0.1" or packet[IP].dst == "192.168.0.1":
            print("!")
            
    if TCP in packet:
        tcp_sport = packet[TCP].sport
        tcp_dport = packet[TCP].dport

        print ("IP src: {}, TCP source port: {}".format(ip_src, tcp_sport))
        print ("IP dst: {}, TCP destination port: {}".format(ip_dst, tcp_dport))


sniff(prn=sniff_packets, store=0)
