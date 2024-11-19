#!/usr/bin/env python3

from scapy.all import *

def print_pkt(pkt):
	pkt.show()

pkt = sniff(iface='br-7b4e746c922f', filter='icmp', prn=print_pkt)
