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
import unittest

class TestGetNetworkAddress(unittest.TestCase):


    def setUp(self):
        from IPAddrLibrary.keywords import Keywords
        self.ipaddrlib = Keywords()

    def test_default_mask(self):
        queryAddress = '192.168.1.24'
        expectAddress = '192.168.1.0'
        resultAddress = self.ipaddrlib.get_network_address(queryAddress)
        print("queried: %s - expected: %s - got: %s" % 
              (queryAddress+'/24',expectAddress,resultAddress))
        self.assertEqual(resultAddress, expectAddress)
    
    def test_dec_mask(self):
        queryAddress = '192.168.1.24'
        queryMask = '255.255.255.0'
        expectAddress = '192.168.1.0'
        resultAddress = self.ipaddrlib.get_network_address(queryAddress,
                                                           queryMask)
        print("queried: %s - expected: %s - got: %s" % 
              (queryAddress+'/'+queryMask,expectAddress,resultAddress))
        self.assertEqual(resultAddress, expectAddress)
        
    def test_smallnet_cidr(self):
        queryAddress = '192.168.1.60'
        queryCidr = '27'
        expectAddress = '192.168.1.32'
        resultAddress = self.ipaddrlib.get_network_address(queryAddress,
                                                           queryCidr)
        print("queried: %s - expected: %s - got: %s" % 
              (queryAddress+'/'+queryCidr,expectAddress,resultAddress))
        self.assertEqual(resultAddress, expectAddress)
        
    def test_smallnet_mask(self):
        queryAddress = '192.168.1.60'
        queryMask = '255.255.255.224'
        expectAddress = '192.168.1.32'
        resultAddress = self.ipaddrlib.get_network_address(queryAddress,
                                                           queryMask)
        print("queried: %s - expected: %s - got: %s" % 
              (queryAddress+'/'+queryMask,expectAddress,resultAddress))
        self.assertEqual(resultAddress, expectAddress)
        
    def test_zero_mask(self):
        queryAddress = '10.10.10.10'
        queryMask = '0'
        expectAddress = '0.0.0.0'
        resultAddress = self.ipaddrlib.get_network_address(queryAddress,
                                                           queryMask)
        print("queried: %s - expected: %s - got: %s" % 
              (queryAddress+'/'+queryMask,expectAddress,resultAddress))
        self.assertEqual(resultAddress, expectAddress)
        
    def test_full_mask(self):
        queryAddress = '10.10.10.10'
        queryMask = '32'
        expectAddress = '10.10.10.10'
        resultAddress = self.ipaddrlib.get_network_address(queryAddress,
                                                           queryMask)
        print("queried: %s - expected: %s - got: %s" % 
              (queryAddress+'/'+queryMask,expectAddress,resultAddress))
        self.assertEqual(resultAddress, expectAddress)

    def test_31_mask(self):
        queryAddress = '10.10.10.10'
        queryMask = '31'
        expectAddress = '10.10.10.10'
        resultAddress = self.ipaddrlib.get_network_address(queryAddress,
                                                           queryMask)
        print("queried: %s - expected: %s - got: %s" % 
              (queryAddress+'/'+queryMask,expectAddress,resultAddress))
        self.assertEqual(resultAddress, expectAddress)
    
        

class TestGetIpFromHostname(unittest.TestCase):

    def setUp(self):
        from IPAddrLibrary.keywords import Keywords
        self.ipaddrlib = Keywords()
    
    def test_fqdn_lookup(self):
        queryHostname = 'google-public-dns-a.google.com'
        expectAddress = '8.8.8.8'
        resultAddress = self.ipaddrlib.get_ip_from_hostname(queryHostname)
        print("queried: %s - expected: %s - got: %s" % 
              (queryHostname,expectAddress,resultAddress))
        self.assertEqual(resultAddress, expectAddress)
    
class TestGetHostnameFromIp(unittest.TestCase):
    
    def setUp(self):
        from IPAddrLibrary.keywords import Keywords
        self.ipaddrlib = Keywords()
    
    def test_fqdn_lookup(self):
        queryAddress = '8.8.8.8'
        expectHostname = 'google-public-dns-a.google.com'
        resultHostname = self.ipaddrlib.get_hostname_from_ip(queryAddress)
        print("queried: %s - expected: %s - got: %s" % 
              (queryAddress,expectHostname,resultHostname))
        self.assertEqual(resultHostname, expectHostname)
        
class TestGetHostnameFromUrl(unittest.TestCase):
    
    def setUp(self):
        from IPAddrLibrary.keywords import Keywords
        self.ipaddrlib = Keywords()
        
    def test_fqdn_url(self):
        queryUrl = 'http://www.google.com'
        expectHostname = 'www.google.com'
        resultHostname = self.ipaddrlib.get_hostname_from_url(url=queryUrl)
        print("queried: %s - expected: %s - got: %s" % 
              (queryUrl,expectHostname,resultHostname))
        self.assertEqual(resultHostname, expectHostname)
    
    def test_nonqual_url(self):
        queryUrl = 'http://google'
        expectHostname = 'google'
        resultHostname = self.ipaddrlib.get_hostname_from_url(url=queryUrl)
        print("queried: %s - expected: %s - got: %s" % 
              (queryUrl,expectHostname,resultHostname))
        self.assertEqual(resultHostname, expectHostname)

    def test_user_url(self):
        queryUrl = 'http://bob:bobbson@www.google.com'
        expectHostname = 'www.google.com'
        resultHostname = self.ipaddrlib.get_hostname_from_url(url=queryUrl)
        print("queried: %s - expected: %s - got: %s" % 
              (queryUrl,expectHostname,resultHostname))
        self.assertEqual(resultHostname, expectHostname)
        
    def test_https_url_with_path_and_port(self):
        queryUrl = 'https://www.google.com:8888/blah/bloo/blee'
        expectHostname = 'www.google.com'
        resultHostname = self.ipaddrlib.get_hostname_from_url(url=queryUrl)
        print("queried: %s - expected: %s - got: %s" % 
              (queryUrl,expectHostname,resultHostname))
        self.assertEqual(resultHostname, expectHostname)

        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
