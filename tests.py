import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.keys import Keys
from resorces import Locators, Url
from selenium.webdriver.support.select import Select


class Main_page(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_zakaz_picy(self):
        self.driver.get(Url.MYYZZAKG)

        ### scroll ###
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, Locators.RIGHT_SCROLL_B)))
        self.driver.find_element_by_css_selector(Locators.RIGHT_SCROLL_B).click()
        self.driver.find_element_by_css_selector(Locators.RIGHT_SCROLL_B).click()
        self.driver.find_element_by_css_selector(Locators.RIGHT_SCROLL_B).click()
        self.driver.find_element_by_css_selector(Locators.RIGHT_SCROLL_B).click()

        ### choose food  category####
        self.driver.find_element_by_css_selector(Locators.FOOD_ICON).click()
        ### choose foods
        self.driver.find_element_by_css_selector(Locators.PLUS_BUTTON1).click()
        self.driver.find_element_by_css_selector(Locators.PLUS_BUTTON2).click()
        self.driver.find_element_by_css_selector(Locators.PLUS_BUTTON3).click()

        ### go to card
        self.driver.find_element_by_css_selector(Locators.CARD_BUTTON).click()

        #### checkout INPUTS

        self.driver.find_element_by_css_selector(Locators.INPUT_NAME).send_keys("Arapbai")
        self.driver.find_element_by_css_selector(Locators.INPUT_NAME).send_keys("773777777")
        self.driver.find_element_by_css_selector(Locators.ORDER_TYPE_PICKUP).click()
        self.driver.find_element_by_css_selector(Locators.ORDER_TYPE_DELIVERY).click()

        self.driver.find_element_by_css_selector(Locators.CITY).click()
        # selecting city
        select_city = Select(self.driver.find_element_by_css_selector(Locators.CITY))
        select_city.select_by_value("10000000000014")

        self.driver.find_element_by_css_selector(Locators.STREET).click()
        self.driver.find_element_by_css_selector(Locators.STREET_SEARCH).send_keys("авиа"+Keys.ENTER)
        self.driver.find_element_by_css_selector(Locators.HOUSE).send_keys("118")
        self.driver.find_element_by_css_selector(Locators.BUILDING).send_keys("/2")
        self.driver.find_element_by_css_selector(Locators.FLOOR).send_keys("8")
        self.driver.find_element_by_css_selector(Locators.ENTRY_CODE).send_keys("14B")
        self.driver.find_element_by_css_selector(Locators.SUMM).send_keys("2000")

        sleep(5)


    def tearDown(self):
            self.driver.close()

if __name__ == "main":
    unittest.main()
