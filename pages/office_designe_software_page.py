from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.locators import office_designe_locators as loc


class OfficeDesigne(BasePage):
    page_url = '/shop/furn-9999-office-design-software-7?category=9'

    def add_to_cart_product(self):
        wait = WebDriverWait(self.driver, 5)
        product_title_on_page = self.find(loc.product_title_on_page_loc)
        name_from_product_page = product_title_on_page.text
        add_to_cart_btn = self.find(loc.add_to_cart_button)
        add_to_cart_btn.click()
        wait.until(EC.text_to_be_present_in_element(loc.product_counter, '1'))
        self.find(loc.cart_button).click()
        product_title_on_cart = wait.until(EC.presence_of_element_located(loc.product_title_on_cart_loc))
        name_from_cart_page = product_title_on_cart.text
        assert name_from_product_page.strip().lower() == name_from_cart_page.strip().lower()

    def change_currency(self):
        wait = WebDriverWait(self.driver, 5)
        self.find(loc.currency_dropdown).click()
        wait.until(EC.visibility_of_element_located(loc.currency_select_EUR)).click()
        currency = self.find(loc.currency_price)
        assert '€' in currency.text

    def open_terms_and_conditions(self):
        wait = WebDriverWait(self.driver, 5)
        self.find(loc.terms_and_condition_link).click()
        tc_headline = wait.until(EC.visibility_of_element_located(loc.terms_headline)).text
        assert 'STANDARD TERMS AND CONDITIONS OF SALE' in tc_headline

    def get_product_in_cart(self):
        wait = WebDriverWait(self.driver, 5)
        self.find(loc.add_to_cart_button).click()
        wait.until(EC.text_to_be_present_in_element(loc.product_counter, '1'))
