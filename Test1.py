from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome("/Users/tminht/PycharmProjects/FiistSeleniumTest/drivers/chromedriver") #test tren trinh duyet nao
# driver = webdriver.Firefox()
# driver = webdriver.Ie()

driver.set_page_load_timeout(10)
driver.get("https://www.google.com.vn/")
driver.find_element_by_name("q").send_keys("Testing")
#driver.find_element_by_name("btnK").click()
driver.find_element_by_name("q").send_keys(Keys.ENTER)
driver.maximize_window()
driver.refresh()

print ('hhhc')
time.sleep(10)
driver.quit()