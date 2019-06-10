import self as self
from selenium import webdriver
from proboscis import test, before_class, after_class
from proboscis.asserts import assert_equal
from proboscis import TestProgram
from selenium.webdriver.common.keys import Keys
import unittest
from proboscis import test
import random
import string
import WebDriverSupport.py
import time
import utils


def support_method():
    pass


class DemoGuRu(unittest.TestCase):
    def randomString(nhap_so_kitu):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(nhap_so_kitu))

    def randomNum(nhapSoLuongNumberVaoDiAThongAhihi):
        nums = string.digits
        return ''.join(random.choice(nums) for i in range(nhapSoLuongNumberVaoDiAThongAhihi))

# random email
    emailNewCustomer = randomString(10)
    emailLogin = randomString(10)
    emailEditCustomer = randomString(4)
    @classmethod
    def setUpClass(self):

        self.driver = webdriver.Chrome("/Users/tminht/PycharmProjects/FiistSeleniumTest/drivers/chromedriver")
        self.driver.get("http://demo.guru99.com/V4/")

    def test_first(self):
        driver = self.driver
        driver.find_element_by_xpath("//a[text()='here']").click()
        driver.find_element_by_xpath("//input[@name='emailid']").send_keys(self.emailLogin + "@gmail.com")
        driver.find_element_by_xpath("//input[@name='emailid']").send_keys(Keys.ENTER)
        userID = driver.find_element_by_xpath("//td[text()='User ID :']//following-sibling::td").text
        passWord = driver.find_element_by_xpath("//td[text()='Password :']//following-sibling::td").text
        driver.back()
        driver.back()
        print("UserID= " + userID)
        print("Password= " + passWord)
        driver.find_element_by_xpath("//input[@name='uid']").send_keys(userID)
        driver.find_element_by_xpath("//input[@name='password']").send_keys(passWord)
        driver.find_element_by_xpath("//input[@name='btnLogin']").click()
        # verify login success
        actual_UserID_Text = driver.find_element_by_xpath("//td[text()='Manger Id : " + userID + "\']").text
        print(actual_UserID_Text)

        assert_equal(actual_UserID_Text, "Manger Id : "+userID)

    # tap add new customer
    def test_second(self):
        driver = self.driver
        driver.find_element_by_xpath("//a[text()='New Customer']").click()
        driver.find_element_by_xpath("//input[@name='name']").send_keys("Thong")
        driver.find_element_by_xpath("//input[@value='m']").click()
        driver.find_element_by_xpath("//textarea[@name='addr']").send_keys("tang bat Ho Q5")
        driver.find_element_by_xpath("//input[@name='city']").send_keys("Ho Chi Minh City")
        driver.find_element_by_xpath("//input[@name='emailid']").send_keys(self.emailNewCustomer + "@gsda.com")
        #  driver.find_element_by_xpath("//input[@name='password']").send_keys(password_SignUp)

        start_date = driver.find_element_by_xpath("//input[@name='dob']")
        start_date.clear()
        start_date.send_keys("08/08/1990")
        driver.find_element_by_xpath("//input[@name='dob']")

        driver.find_element_by_xpath("//input[@name='state']").send_keys("Ho chi minh")
        driver.find_element_by_xpath("//input[@name='pinno']").send_keys("123456")
        driver.find_element_by_xpath("//input[@name='telephoneno']").send_keys("0988845885")

        driver.find_element_by_xpath("//input[@value='Submit']").click()

        # verify add new customer thành công
        verify_NewCustomer = driver.find_element_by_xpath("//p[text()='Customer Registered Successfully!!!']").text
        if (verify_NewCustomer == "Customer Registered Successfully!!!"):
            print("Tạo mới thành công")
        else:
            print("Failed")

    # edit customer
    def test_three(self):
        driver = self.driver
        f = driver.find_element_by_xpath("//td[text()='Customer ID']//following-sibling::td").text
        driver.find_element_by_xpath("//a[text()='Edit Customer']").click()
        driver.find_element_by_xpath("//input[@name='cusid']").send_keys(f)
        driver.find_element_by_xpath("//input[@name='AccSubmit']").click()

        driver.find_element_by_xpath("//textarea[@name='addr']").clear()
        driver.find_element_by_xpath("//textarea[@name='addr']").send_keys("Tettt")

        driver.find_element_by_xpath("//input[@name='city']").clear()
        driver.find_element_by_xpath("//input[@name='city']").send_keys("Quan Tan Binh")

        driver.find_element_by_xpath("//input[@name='pinno']").clear()
        driver.find_element_by_xpath("//input[@name='pinno']").send_keys(self.randomNum(6))

        driver.find_element_by_xpath("//input[@name='emailid']").clear()
        driver.find_element_by_xpath("//input[@name='emailid']").send_keys("thong" + self.emailEditCustomer + "@gmail.com")

        driver.find_element_by_xpath("//input[@name='sub']").click()

    @classmethod
    def tearDownClass(self):
        driver = self.driver
        driver.quit()
        # print(driver.find_element_by_xpath("//input[@name='name']").text)

    # print(old_string)

if __name__ == "__main__":
    unittest.main()
