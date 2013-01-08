import iplib
import socket
class Keywords(object):
    
    
    def get_network_address(self, ipaddr, mask="24"):
        """
        Gets the network address from the given ipaddr and mask
        
        If mask is not given, it is assumed to me be a 24-bit mask (i.e. 255.255.255.0)
        
        ipaddr must be in the form a.b.c.d (currently only IPv4 addresses are supported)
        mask can be in the form x.x.x.x or mask length (number from 0 to 32)
        """
        cidr = iplib.CIDR(ipaddr, mask)
        netmask_bits = cidr.get_netmask().get_bits()
        if netmask_bits in ('31','32'):
            """return IP if there is no real network/broadcast address"""
            netaddr = cidr.get_ip()
        else:
            netaddr = cidr.get_network_ip()
        return netaddr

    
    def get_ip_from_hostname(self, hostname):
        addr = socket.gethostbyname(hostname)
        return addr

    
    def get_hostname_from_ip(self, address):
        host = socket.gethostbyaddr(address)
        return host[0]
    
    
    
    
    
    



