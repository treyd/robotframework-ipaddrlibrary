import iplib
class Keywords(object):
    
    
    def get_network_address(self, ipaddr, mask="24"):
        cidr = iplib.CIDR(ipaddr, mask)
        netaddr = cidr.get_network_ip()
        return netaddr
    
    



