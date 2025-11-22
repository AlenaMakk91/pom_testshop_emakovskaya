from selenium.webdriver import Keys

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.locators import section_desc_locators as loc


class Section_Desc_Page(BasePage):
    page_url = '/shop/category/desks-1'

    def search_items(self, text):
        search_field = self.find(loc.search_field)
        search_field.send_keys(text)
        search_field.send_keys(Keys.ENTER)
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(loc.result_count))
        results = self.find_all(loc.result_products)
        for product in results:
            content_attr = product.get_attribute('content')
            assert text.lower() in content_attr.lower(), "Невалидные результаты поиска"

    def sort_items_by_name(self):
        self.driver.implicitly_wait(5)
        dropdown = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(loc.sort_dropdown)
        )
        dropdown.click()
        sorting_by_name = self.find(loc.sort_by_name)
        sorting_by_name.click()
        results = self.find_all(loc.result_products)
        product_names = []
        for product in results:
            content_attr = product.get_attribute('text')
            product_names.append(content_attr)
        assert product_names == sorted(product_names)

    def filter_by_price(self, min_price, max_price):
        self.driver.implicitly_wait(5)
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(loc.field_min)
        ).click()
        min_price_set = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(loc.input_min)
        )
        min_price_set.send_keys(min_price)
        min_price_set.send_keys(Keys.ENTER)

        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(loc.field_max)
        ).click()
        max_price_set = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(loc.input_max)
        )
        max_price_set.send_keys(max_price)
        max_price_set.send_keys(Keys.ENTER)

        results = self.find_all(loc.product_price)
        for item in results:
            price_attr = item.text
            price_result = float(price_attr.replace(',', ''))
            assert max_price >= price_result >= min_price
