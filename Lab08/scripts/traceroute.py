#!/usr/bin/env python3

from scapy.all import *

def traceroute(destination, max_hops=30, timeout=2):
    print(f"Traceroute to {destination}, max {max_hops} hops:")
    
    for ttl in range(1, max_hops + 1):
        pkt = IP(dst=destination, ttl=ttl) / ICMP()
        reply = sr1(pkt, verbose=0, timeout=timeout)
        
        if reply is None:
            print(f"{ttl}\t*")
        elif reply.type == 0:  # Echo Reply
            print(f"{ttl}\t{reply.src}\t(Destination reached)")
            break
        elif reply.type == 11:  # Time Exceeded
            print(f"{ttl}\t{reply.src}")
        else:
            print(f"{ttl}\t{reply.src}\t(Unexpected response)")
            break

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python3 traceroute.py <destination>")
        sys.exit(1)
    
    destination = sys.argv[1]
    traceroute(destination)
