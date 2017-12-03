#!/usr/bin/python3
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
import requests

ct_packets = 0
ct_source_add_counter = 0
sf_packets = 0
sf_source_add_counter = 0

def detection(pkt):
    global ct_packets
    global ct_source_add_counter
    global sf_packets
    global sf_source_add_counter

    F = pkt.sprintf('%TCP.flags%')
    Dst = pkt.sprintf('%IP.dst%')
    Src = pkt.sprintf('%IP.src%')

    # Checks if there are the correct flags shown for the Xmas Attack
    if F == "FPU":
        ct_packets += 1

        if ct_packets == 50:
            ct_packets = 0
            print('Christmas Tree Attack detected.')
            send_notification('Christmas Tree Attack', Dst, Src, 'Moderate')

    # Checks if there are the correct flags shown for the Xmas Attack
    if F == "SA":
        sf_packets += 1

        if sf_packets == 50:
            sf_packets = 0
            print('SYN Flood Attack detected.')
            send_notification('SYN Flood Attack', Dst, Src, 'Severe')


def send_notification(attack, dst, src, threat_level):
    URL = 'http://localhost:8000/notifications/'

    client = requests.session()

    # Retrieve the CSRF token first
    client.get(URL)  # sets cookie
    csrftoken = client.cookies['csrftoken']

    notification_data = {
        'attack': attack,
        'dest_address': dst,
        'source_address': src,
        'threat_level': threat_level,
        'csrfmiddlewaretoken': csrftoken,
    }

    r = client.post(URL, data=notification_data)
    print(r.text)

if __name__ == '__main__':
    sniff(prn=detection, filter='tcp', store=0)
