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
        time.sleep(3)

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
        time.sleep(1)

    def testcase3(self):
        '''
        Проверка поиска существующего товара
        '''
        driver = self.driver
        driver.get('https://www.e-katalog.ru/')
        elem = driver.find_element_by_xpath('//input[@id="ek-search"]')
        elem.send_keys('PlayStation 4')
        time.sleep(0.5)
        driver.find_element_by_xpath('//button[@name="search_but_"]').click()
        time.sleep(2)
    
    def testcase4(self):
        '''
        Проверка поиска несуществующего товара
        '''
        driver = self.driver
        driver.get('https://www.e-katalog.ru/')
        elem = driver.find_element_by_xpath('//input[@id="ek-search"]')
        elem.send_keys('PlayStation 98765')
        time.sleep(0.5)
        driver.find_element_by_xpath('//button[@name="search_but_"]').click()
        time.sleep(2)

    def testcase5(self):
        '''
        Регистрация подходящего профиля с валидными данными
        '''
        driver = self.driver
        driver.get('https://www.e-katalog.ru/')
        driver.find_element_by_xpath('//span[@class="wu_entr"]').click()
        time.sleep(0.5)
        driver.find_element_by_xpath('//span[@class="j-wrap orange"]/em').click()
        time.sleep(0.5)
        elem1 = driver.find_element_by_xpath('//div[@class="registration-name ek-form-group"]/input')
        elem2 = driver.find_element_by_xpath('//div[@class="registration-email ek-form-group"]/input')
        elem3 = driver.find_element_by_xpath('//div[@class="registration-password ek-form-group"]/input')

        elem1.send_keys('namenamename')
        elem2.send_keys('name123123@gmail.com')
        elem3.send_keys('sdrtfcijnk')

        time.sleep(0.5)

        driver.find_element_by_xpath('//div[@class="registration-actions r-text"]/button[2]').click()
        
        time.sleep(3)

    def testcase6(self):
        '''
        Регистрация неподходящего профиля с invalidными данными
        '''
        driver = self.driver
        driver.get('https://www.e-katalog.ru/')
        driver.find_element_by_xpath('//span[@class="wu_entr"]').click()
        time.sleep(0.5)
        driver.find_element_by_xpath('//span[@class="j-wrap orange"]/em').click()
        time.sleep(0.5)
        elem1 = driver.find_element_by_xpath('//div[@class="registration-name ek-form-group"]/input')
        elem2 = driver.find_element_by_xpath('//div[@class="registration-email ek-form-group"]/input')
        elem3 = driver.find_element_by_xpath('//div[@class="registration-password ek-form-group"]/input')

        elem1.send_keys('navvvvvvvvvvvvvvvvvvvvenamename')
        elem2.send_keys('name12ygvhbjnkm,bfduibfdoij3123@ghgfdsbfdbfds;lkjbdmail.com')
        elem3.send_keys('sdrk')

        time.sleep(0.5)

        driver.find_element_by_xpath('//div[@class="registration-actions r-text"]/button[2]').click()
        
        time.sleep(3)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()