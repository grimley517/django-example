from selenium import webdriver
import unittest

class tests(unittest.TestCase):
    
    def setup(self):
        self.browser = webdriver.Chrome()
        
    
    def teardown(self):
        self.browser.quit()
        
    def test1(self):
        self.browser.get('http://$IP:$PORT')
        assert 'django' in self.browser.title

if __name__ == '__main__':
    unittest.main()