import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst = ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_rqst_broadcast = broadcast/arp_request
    answered = scapy.srp(arp_rqst_broadcast,timeout = 2, verbose = False)[0]
    for answer in answered:
        print("ip: ",answer[1].psrc,"mac: ",answer[1].hwsrc)

scan("192.168.1.1/24")

