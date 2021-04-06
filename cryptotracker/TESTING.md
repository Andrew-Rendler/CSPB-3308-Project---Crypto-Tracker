# Testing
  - Steps to run:
      1. `cd cryptotracker`
      2. `. venv/bin/activate`
      3. `pip3 install -r requirements.txt`
      4. `python3 CryptoDataUnitTest.py` 
      4. `python3 CryptoCompareAPIUnitTest.py` 

### CryptoCompareAPIUnitTeset

### Use case name
  - Test Instantiation of CryptoCompareAPI
    
### Description
  - Tests Instantiation of CryptoCompareAPI
    
### Test steps
  1. Create a new instance on CryptoCompareAPI2
  2. Test the Historical endpoint
  3. Test the News endpoint
  4. Test the Current Price endpoint
  5. Test the rate limit endpoint

### Expected result
   1. CryptoCompareAPI should exist and the value should not be None
   2. All other tests should return a 200 status code
  
### Actual result
  - Above expectations are met on all test cases
  
##### Status (Pass/Fail)
  - Pass