from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import string
import time

#random email
def randomString(stringLength=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))
z = randomString(10)
print("String", randomString(10))

#sign up and login
driver = webdriver.Chrome("/Users/tminht/PycharmProjects/FiistSeleniumTest/drivers/chromedriver")
driver.get("http://demo.guru99.com/V4/")
driver.find_element_by_xpath("//a[text()='here']").click()
driver.find_element_by_xpath("//input[@name='emailid']").send_keys("thong123@test.com")
driver.find_element_by_xpath("//input[@name='emailid']").send_keys(Keys.ENTER)
a = driver.find_element_by_xpath("//td[text()='User ID :']//following-sibling::td").text
b = driver.find_element_by_xpath("//td[text()='Password :']//following-sibling::td").text
driver.back()
driver.back()
print(a)
print(b)
driver.find_element_by_xpath("//input[@name='uid']").send_keys(a)
driver.find_element_by_xpath("//input[@name='password']").send_keys(b)

driver.find_element_by_xpath("//input[@name='btnLogin']").click()
#verify login success
c = driver.find_element_by_xpath("//td[text()='Manger Id : mngr198979']").text
d = "Manger Id : mngr198979"
if (c == d):
    print("Thành công")
else :
    print("Failed")
time.sleep(2)

#tap add new customer
driver.find_element_by_xpath("//a[text()='New Customer']").click()
driver.find_element_by_xpath("//input[@name='name']").send_keys("Thong")
driver.find_element_by_xpath("//input[@value='m']").click()
driver.find_element_by_xpath("//textarea[@name='addr']").send_keys("tang bat Ho Q5")
driver.find_element_by_xpath("//input[@name='city']").send_keys("Ho Chi Minh City")
driver.find_element_by_xpath("//input[@name='emailid']").send_keys(z + "@gsda.com")
driver.find_element_by_xpath("//input[@name='password']").send_keys(b)

start_date = driver.find_element_by_xpath("//input[@name='dob']")
start_date.clear()
start_date.send_keys("08/08/1990")
driver.find_element_by_xpath("//input[@name='dob']")

driver.find_element_by_xpath("//input[@name='state']").send_keys("Ho chi minh")
driver.find_element_by_xpath("//input[@name='pinno']").send_keys("12345678")
driver.find_element_by_xpath("//input[@name='telephoneno']").send_keys("098884588534")

driver.find_element_by_xpath("//input[@value='Submit']").click()


#verify add new customer thành công
e = driver.find_element_by_xpath("//p[text()='Customer Registered Successfully!!!']").text
if (e == "Customer Registered Successfully!!!"):
    print("Tạo mới thành công")
else:
    print("Failed")

#edit customer
f = driver.find_element_by_xpath("//td[text()='Customer ID']//following-sibling::td").text
driver.find_element_by_xpath("//a[text()='Edit Customer']").click()
driver.find_element_by_xpath("//input[@name='cusid']").send_keys(f)
driver.find_element_by_xpath("//input[@name='AccSubmit']").click()


#print(driver.find_element_by_xpath("//input[@name='name']").text)

#print(old_string)


#driver.find_element_by_xpath("//input[@name='name']").clear()



