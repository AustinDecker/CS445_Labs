from scapy.all import *
a = IP();
a.src = "10.0.2.15"
a.dst = "11.22.33.44"
b = ICMP()
p = a/b
send(p)
