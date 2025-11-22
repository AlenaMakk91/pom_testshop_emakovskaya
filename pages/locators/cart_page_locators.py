from selenium.webdriver.common.by import By

empty_message = (By.CSS_SELECTOR, '[class="js_cart_lines alert alert-info"]')
input_counter = (By.CSS_SELECTOR, '[class="js_quantity quantity form-control border-start-0 border-end-0"]')
product_price = (By.XPATH, '//*[@id="cart_products"]/div/div[3]/div[2]/span/span')
quantity_input = (By.XPATH, '//*[@id="cart_products"]/div/div[3]/div[1]/input')
product_counter = (By.XPATH, '//*[@id="o_main_nav"]/ul[2]/li[2]/a/div/sup')
discount_code = (By.CSS_SELECTOR, '[placeholder="Discount code..."]')
error_message = (By.CSS_SELECTOR, '[class="alert alert-danger text-start"]')
