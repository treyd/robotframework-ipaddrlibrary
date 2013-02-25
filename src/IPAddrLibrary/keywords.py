#-------------------------------------------------------------------------------
# Copyright 2013 Maldivica, Inc (www.maldivica.com)
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#   http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#-------------------------------------------------------------------------------
'''
Created on Jan 3, 2013

@author: Trey Duskin <trey@maldivica.com>
'''

import iplib
import socket

class Keywords(object):
    """Keywords class contains all externally-facing Robot keywords"""
    
    def get_network_address(self, ipaddr, mask="24"):
        """
        Gets the network address from the given _ipaddr_ and _mask_
        
        If _mask_ is not given, it is assumed to be a 24-bit mask 
        (i.e. 255.255.255.0)
        
        _ipaddr_ must be in the form a.b.c.d (currently only IPv4 addresses 
        are supported)
        
        _mask_ can be in the form x.x.x.x or mask length (number from 0 to 32)
        """
        cidr = iplib.CIDR(ipaddr, mask)
        netmask_bits = cidr.get_netmask().get_bits()
        if netmask_bits in ('31','32'):
            # return IP if there is no real network/broadcast address
            netaddress = cidr.get_ip()
        else:
            netaddress = cidr.get_network_ip()
        return netaddress

    
    def get_ip_from_hostname(self, hostname):
        """Gets the IP address for the given _hostname_"""
        addr = socket.gethostbyname(hostname)
        return addr

    
    def get_hostname_from_ip(self, address):
        """Gets the hostname for the given _address_"""
        (host, aliases, addr) = socket.gethostbyaddr(address)
        return host

    
    def get_hostname_from_url(self, url):
        """
        Gets the hostname from given _url_
        
        Will filter out any protocol, paths, usernames and passwords, and 
        port numbers in the _url_ string
        
        E.g:
        | ${host1} = | Get Hostname from URL | http://www.google.com/images |
        | ${host2} = | Get Hostname from URL | ftp://bob:pass@ftp.site.net/ |
        | ${host3} = | Get Hostname from URL | https://proxy:8080 |
        =>
        | ${host1} = 'www.google.com'
        | ${host2} = 'ftp.site.net'
        | ${host3} = 'proxy'
        """
        # split url based on slashes
        url_split = url.split('/')
        
        # iterate through split list and discard protocol
        filterlist = ['http:', 'https:', 'ftp:', '']
        cleaned_split_url = [ value for value in url_split if 
                             value not in filterlist]
        
        # host info will be first element
        host = cleaned_split_url[0]
        
        # split out username/pass, if any. anything after the '@' is 
        # considered a host
        host_split = host.split('@')
        host_nouser = host_split[-1]
        
        # split out port, if any
        host_split = host_nouser.split(':')
        cleaned_host = host_split[0]
        
        return cleaned_host
    
    
    
    
    
    
    
    



