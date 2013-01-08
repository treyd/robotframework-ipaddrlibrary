'''
Created on Jan 3, 2013

@author: Trey Duskin
'''
import unittest

class TestGetNetworkAddress(unittest.TestCase):


    def setUp(self):
        from IPAddrLibrary.Keywords import Keywords
        self.ipaddrlib = Keywords()

    def test_default_mask(self):
        queryAddress = '192.168.1.24'
        expectAddress = '192.168.1.0'
        resultAddress = self.ipaddrlib.get_network_address(queryAddress)
        print "queried: %s - expected: %s - got: %s" % (queryAddress+'/24',expectAddress,resultAddress)
        self.assertEqual(resultAddress, expectAddress)
    
    def test_dec_mask(self):
        queryAddress = '192.168.1.24'
        queryMask = '255.255.255.0'
        expectAddress = '192.168.1.0'
        resultAddress = self.ipaddrlib.get_network_address(queryAddress,queryMask)
        print "queried: %s - expected: %s - got: %s" % (queryAddress+'/'+queryMask,expectAddress,resultAddress)
        self.assertEqual(resultAddress, expectAddress)
        
    def test_smallnet_cidr(self):
        queryAddress = '192.168.1.60'
        queryCidr = '27'
        expectAddress = '192.168.1.32'
        resultAddress = self.ipaddrlib.get_network_address(queryAddress,queryCidr)
        print "queried: %s - expected: %s - got: %s" % (queryAddress+'/'+queryCidr,expectAddress,resultAddress)
        self.assertEqual(resultAddress, expectAddress)
        
    def test_smallnet_mask(self):
        queryAddress = '192.168.1.60'
        queryMask = '255.255.255.224'
        expectAddress = '192.168.1.32'
        resultAddress = self.ipaddrlib.get_network_address(queryAddress,queryMask)
        print "queried: %s - expected: %s - got: %s" % (queryAddress+'/'+queryMask,expectAddress,resultAddress)
        self.assertEqual(resultAddress, expectAddress)
    
    
        

class TestGetIpFromHostname(unittest.TestCase):

    def setUp(self):
        from IPAddrLibrary.Keywords import Keywords
        self.ipaddrlib = Keywords()
    
    def test_fqdn_lookup(self):
        queryHostname = 'google-public-dns-a.google.com'
        expectAddress = '8.8.8.8'
        resultAddress = self.ipaddrlib.get_ip_from_hostname(queryHostname)
        print "queried: %s - expected: %s - got: %s" % (queryHostname,expectAddress,resultAddress)
        self.assertEqual(resultAddress, expectAddress)
    
class TestGetHostnameFromIp(unittest.TestCase):
    
    def setUp(self):
        from IPAddrLibrary.Keywords import Keywords
        self.ipaddrlib = Keywords()
    
    def test_fqdn_lookup(self):
        queryAddress = '8.8.8.8'
        expectHostname = 'google-public-dns-a.google.com'
        resultHostname = self.ipaddrlib.get_hostname_from_ip(queryAddress)
        print "queried: %s - expected: %s - got: %s" % (queryAddress,expectHostname,resultHostname)
        self.assertEqual(resultHostname, expectHostname)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()