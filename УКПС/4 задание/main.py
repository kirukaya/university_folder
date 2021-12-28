import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

class TestBrowser(unittest.TestCase):

    def setUp(self):
        WINDOW_SIZE = '1400,800' 
        chrome_options = Options()    
        chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)    
        self.driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=chrome_options)

    def testcase1(self):
        '''
        Проверка смены региона
        '''
        driver = self.driver
        driver.get('https://www.e-katalog.ru/')
        driver.find_element_by_xpath('//div[@class="ib h"]').click()
        time.sleep(0.5)
        elem = driver.find_element_by_xpath('//div[@class="posr"]/input')
        elem.send_keys("Санкт-Петербург")
        time.sleep(0.5)
        driver.find_element_by_xpath('//td[@class="city"]').click()

    def testcase2(self):
        '''
        Проверка перехода на соцсети в footer'е
        '''
        driver = self.driver
        driver.get('https://www.e-katalog.ru/')
        time.sleep(0.1)
        parent_handle  = driver.window_handles[0]
        driver.find_element_by_xpath('//a[@class="social-link social-link-youtube"]').click()
        driver.switch_to.window(parent_handle)
        driver.find_element_by_xpath('//a[@class="social-link social-link-vk"]').click()
        driver.switch_to.window(parent_handle)
        driver.find_element_by_xpath('//a[@class="social-link social-link-facebook"]').click()
        driver.switch_to.window(parent_handle)
        driver.find_element_by_xpath('//a[@class="social-link social-link-instagram"]').click()
        driver.switch_to.window(parent_handle)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    WINDOW_SIZE = '1400,800' 
    chrome_options = Options()    
    chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)    
    driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=chrome_options)
    
    
    # unittest.main()