#!/usr/bin/python3
import unittest
import CryptoData
import re

class CryptoDataTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass


    def tearDown(self):
        pass

    def test_init(self):
        '''Verify API call works and data is stored in member variables'''
        cryptodata = CryptoData.CryptoData()
        self.assertGreater(len(cryptodata.dataList), 0, "dataList should have length greater than 0")
        self.assertGreater(cryptodata.currentPrice, 0, "currentPrice should equal BTC price")
        self.assertGreater(cryptodata.previousClose, 0, "previousClose should equal BTC price from yesterday")
        self.assertGreater(len(cryptodata.volumeList), 0, "volumeList should have length greater than 0")

    def test_getDic(self):
        '''Verify a dict of length 4 is returned with correct keys/values'''
        cryptodata = CryptoData.CryptoData()
        self.assertEqual(len(cryptodata.getDic()), 4,
                         "getDic method returned dictionary of wrong size")
        self.assertEqual(cryptodata.getDic()['Price'], cryptodata.currentPrice,
                         "['Price'] key's value is incorrect")
        self.assertEqual(cryptodata.getDic()["Percent Change"], cryptodata.percentChange(),
                         "Key's value is incorrect")
        
    def test_percentChange(self):
        '''Verify percentChange returns a string of format "x.xx%" or "-x.xx%" '''
        cryptodata = CryptoData.CryptoData()
        percent = re.compile(r'^(\-){0,1}[0-9]{0,5}[\.]{1}[0-9]{2}[\%]$')
        self.assertNotEqual(percent.match(cryptodata.percentChange()), None,
                            "Return value formatted incorrectly")
        
    def test_dollarChange(self):
        '''Verify dollarChange returns a string of format "+x.xx" or "-x.xx" '''
        cryptodata = CryptoData.CryptoData()
        dollar = re.compile(r'^(\-|\+)[0-9]*[\.]{1}[0-9]{2}$')
        self.assertNotEqual(dollar.match(cryptodata.dollarChange()), None,
                            "Return value formatted incorrectly") 

    def test_marketCap(self):
        '''Verify marketCap returns a string of format "x.xxxM", "x.xxxB", or "x.xxxT" '''
        cryptodata = CryptoData.CryptoData()
        dollar = re.compile(r'^[0-9]*[\.]{1}[0-9]{3}(M|B|T)$')
        self.assertNotEqual(dollar.match(cryptodata.marketCap()), None,
                            "Return value formatted incorrectly")

    def test_averageVolume(self):
        '''Verify averageVolume returns a string of format "x.xx" '''
        cryptodata = CryptoData.CryptoData()
        dollar = re.compile(r'^[0-9]*[\.]{1}[0-9]{2}$')
        self.assertNotEqual(dollar.match(cryptodata.averageVolume()), None,
                            "Return value formatted incorrectly") 

if __name__ == '__main__':
    unittest.main()
