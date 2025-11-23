import random
import re

from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.locators import cart_page_locators as loc


class CartPage(BasePage):
    page_url = '/shop/cart'
    text = 'Your cart is empty!'

    def empty_cart_message(self, text=None):
        text = text if text else self.text
        empty_msg_text = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(loc.empty_message))
        assert empty_msg_text.text == text

    def change_product_quantity_and_verify_total_price(self):
        wait = WebDriverWait(self.driver, 5)

        one_product_price_text = self.find(loc.product_price).text
        one_product_price = float(re.search(r"([\d,.]+)", one_product_price_text.replace(',', '.'))[1])

        quantity = random.randint(1, 3)
        quantity_field = self.find(loc.quantity_input)
        quantity_field.click()
        quantity_field.clear()
        quantity_field.send_keys(quantity)
        quantity_field.send_keys(Keys.ENTER)

        wait.until(EC.text_to_be_present_in_element(loc.product_counter, str(quantity)))

        final_price_text = self.find(loc.product_price).text
        final_price_value = float(re.search(r"([\d,.]+)", final_price_text.replace(',', '.'))[1])

        expected_price = round(one_product_price * quantity, 2)
        assert final_price_value == expected_price

    def check_invalid_promo(self):
        wait = WebDriverWait(self.driver, 5)
        promo = 'test'
        input_promo = self.find(loc.discount_code)
        input_promo.click()
        input_promo.send_keys(promo)
        input_promo.send_keys(Keys.ENTER)
        text_error_message = wait.until(EC.visibility_of_element_located(loc.error_message)).text
        assert 'This promo code is not available.' in text_error_message
