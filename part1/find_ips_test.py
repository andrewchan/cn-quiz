from unittest2 import TestCase
from find_ips import find_ips

class FindIpTests(TestCase):

    def test_nothing_match(self):
        self.assertListEqual(find_ips(None), [])
        self.assertListEqual(find_ips(''), [])
        self.assertListEqual(find_ips('nothing to match here'), [])
        self.assertListEqual(find_ips('192.168.1.1is not a match'), [])
        self.assertListEqual(find_ips('this 192.166.1.1is not a match'), [])

    def test_match_one_valid_ipv4(self):
        ips = [ '192.168.0.1',
                '12.12.2.1',
                '0.0.0.0',
                '255.255.255.255'
        ]
        for ip in ips:
            expected = [ip]
            self.assertListEqual(find_ips(ip), expected)
            self.assertListEqual(find_ips("%s at the beginning of string" % ip), expected, "Unable to find ip %s at the beginning" % ip)
            self.assertListEqual(find_ips("test ip is %s in the middle of the string" % ip), expected, "Unable to find ip %s in the middle of the string" % ip)
            self.assertListEqual(find_ips("test ip at the end of the string %s" % ip), expected, "Unable to find ip %s at the end of the string" % ip)

    def test_multiple_matches(self):
        ip1 = '192.168.0.199'
        ip2 = '10.0.0.1'
        ip3 = '98.41.32.1'
        expected = [ip1, ip2, ip3]
        self.assertListEqual(find_ips("%s is first match, %s second and here is the third %s" % (ip1, ip2, ip3)), expected)
        

    def test_invalid_ipv4_addr(self):
        ips = [ '.1.2.3',
                '1..2.3',
                '1..3',
                '..2.',
                '-1.2.3.4',
                '192.256.1.1',
                '255.255.255.256',
                '1234.123.3.11',
                '_123.123.24.3'
        ]

        for ip in ips:
            not_expected = [ip]
            self.assertNotEqual(find_ips("IP %s is invalid" % ip), not_expected, "Invalid ipv4 address %s was matched" % ip)

    def test_match_in_multiple_line_string(self):
        ip = '192.168.1.1'
        big_doc = '''
        %s This is a big doc. This is a big doc. This is a big doc. This is a big doc. 
        This is a big doc. This is a big doc. This is a big doc. This is a big doc. This is a big doc. 
        This is a big doc. This is a big doc. This is a big doc. This is a big doc. This is a big doc. 
        This is a big doc. %s This is a big doc. This is a big doc. This is a big doc. This is a big doc. 
        This is a big doc. This is a big doc. This is a big doc. This is a big doc. This is a big doc. %s
        This is a big doc. This is a big doc. This is a big doc. This is a big doc. This is a big doc. 
        %s This is a big doc. This is a big doc. This is a big doc. This is a big doc. This is a big doc. 
        %s
        ''' % (ip, ip, ip, ip, ip)
        expected = [ip, ip, ip, ip, ip]
        self.assertListEqual(find_ips(big_doc), expected)