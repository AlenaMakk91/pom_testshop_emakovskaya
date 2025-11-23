import random

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.locators import multimedia_category_locators as loc


class OfficeDesigne(BasePage):
    page_url = '/shop/category/multimedia-9'

    def add_product_to_cart_and_verify(self):
        wait = WebDriverWait(self.driver, 5)

        products = self.find_all(loc.result_products)
        product_for_test = random.choice(products)
        product_for_test.click()

        product_title_on_page = self.find(loc.product_title_on_page_loc)
        name_from_product_page = product_title_on_page.text
        add_to_cart_btn = self.find(loc.add_to_cart_button)
        add_to_cart_btn.click()
        wait.until(EC.text_to_be_present_in_element(loc.product_counter, '1'))
        self.find(loc.cart_button).click()
        product_title_on_cart = wait.until(EC.presence_of_element_located(loc.product_title_on_cart_loc))
        name_from_cart_page = product_title_on_cart.text
        assert name_from_product_page.strip().lower() == name_from_cart_page.strip().lower()

    def change_currency_to_eur_and_verify(self):
        wait = WebDriverWait(self.driver, 5)

        products = self.find_all(loc.result_products)
        product_for_test = random.choice(products)
        product_for_test.click()

        self.find(loc.currency_dropdown).click()
        wait.until(EC.visibility_of_element_located(loc.currency_select_EUR)).click()
        currency = self.find(loc.currency_price)
        assert '€' in currency.text

    def open_terms_and_conditions(self, text):
        wait = WebDriverWait(self.driver, 5)

        products = self.find_all(loc.result_products)
        product_for_test = random.choice(products)
        product_for_test.click()

        self.find(loc.terms_and_condition_link).click()
        tc_headline = wait.until(EC.visibility_of_element_located(loc.terms_headline)).text
        assert text in tc_headline

    def add_product_to_cart(self):
        wait = WebDriverWait(self.driver, 5)

        products = self.find_all(loc.result_products)
        product_for_test = random.choice(products)
        product_for_test.click()

        self.find(loc.add_to_cart_button).click()
        wait.until(EC.text_to_be_present_in_element(loc.product_counter, '1'))
