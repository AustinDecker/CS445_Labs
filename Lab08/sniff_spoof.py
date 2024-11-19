#!/usr/bin/env python3
from scapy.all import *

def intercept_pkt(pkt):
    if(pkt[2].type == 8):
        src = pkt[1].src
        dst = pkt[1].dst
        seq = pkt[2].seq
        id = pkt[2].id
        load = pkt[3].load
        
        reply = IP(src=dst, dst=src) / ICMP(type=0, id=id, seq=seq) / load
        send(reply)

pkt = sniff(iface='br-7b4e746c922f',filter = 'icmp', prn=intercept_pkt)
