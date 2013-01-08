import iplib
import socket
class Keywords(object):
    
    
    def get_network_address(self, ipaddr, mask="24"):
        cidr = iplib.CIDR(ipaddr, mask)
        netaddr = cidr.get_network_ip()
        return netaddr

    
    def get_ip_from_hostname(self, hostname):
        addr = socket.gethostbyname(hostname)
        return addr

    
    def get_hostname_from_ip(self, address):
        host = socket.gethostbyaddr(address)
        return host[0]
    
    
    
    
    
    



