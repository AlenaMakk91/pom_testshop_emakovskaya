from selenium.webdriver.common.by import By

search_field = (By.XPATH, '//*[@id="products_grid"]/div[1]/form/div/input')
result_products = (By.CSS_SELECTOR, '.text-primary.text-decoration-none')
result_count = (By.XPATH, '//*[@id="products_grid"]/div[1]/form/div/button/span/small')
sort_dropdown = (By.XPATH, '//*[@id="products_grid"]/div[1]/div[2]/a/span[1]')
sort_by_name = (By.XPATH, '//*[@id="products_grid"]/div[1]/div[2]/div/a[3]/span')
field_min = (By.CSS_SELECTOR, '[class="multirange-min position-absolute opacity-75 opacity-100-hover mt-1"]')
field_max = (By.CSS_SELECTOR, '[class="multirange-max position-absolute opacity-75 opacity-100-hover mt-1 end-0"]')
input_min = (By.CSS_SELECTOR, '[class="form-control form-control-sm mb-2 mb-lg-1 multirange-min"]')
input_max = (By.CSS_SELECTOR, '[class="form-control form-control-sm mb-2 mb-lg-1 multirange-max"]')
product_price = (By.CSS_SELECTOR, '.oe_currency_value')
add_item_to_cart = (By.CSS_SELECTOR, '[class="btn btn-primary a-submit"]')
