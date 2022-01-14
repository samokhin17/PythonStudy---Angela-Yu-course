# -*- coding: utf-8 -*-
import unittest

from selenium import webdriver


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)

    def test_contact_creation(self):
        self.login()
        self.create()
        self.logout()

    def logout(self):
        driver = self.driver
        driver.find_element_by_link_text("Logout").click()

    def return_to_groups_page(self):
        driver = self.driver
        driver.find_element_by_link_text("group page").click()

    def create(self):
        driver = self.driver
        self.go_to_groups_page()
        # Init group creation
        driver.find_element_by_name("new").click()
        # Fill group form
        driver.find_element_by_name("group_name").click()
        driver.find_element_by_name("group_name").clear()
        driver.find_element_by_name("group_name").send_keys("777")
        driver.find_element_by_name("group_header").click()
        driver.find_element_by_name("group_header").clear()
        driver.find_element_by_name("group_header").send_keys("777")
        driver.find_element_by_name("group_footer").click()
        driver.find_element_by_name("group_footer").clear()
        driver.find_element_by_name("group_footer").send_keys("777")
        # Submit group creation
        driver.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def go_to_groups_page(self):
        driver = self.driver
        driver.find_element_by_link_text("groups").click()

    def login(self):
        driver = self.driver
        self.open_home_page()
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("admin")
        driver.find_element_by_name("pass").click()
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys("secret")
        driver.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
