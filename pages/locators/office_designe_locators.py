from selenium.webdriver.common.by import By

add_to_cart_button = (By.ID, 'add_to_cart')
terms_and_condition_link = (By.LINK_TEXT, 'Terms and Conditions')
cart_button = (By.XPATH, '//*[@id="o_main_nav"]/ul[2]/li[2]/a/div/i')
product_title_on_cart_loc = (By.CSS_SELECTOR, '[class="d-inline align-top h6 fw-bold"]')
product_title_on_page_loc = (By.CSS_SELECTOR, '#product_details > h1')
product_counter = (By.XPATH, '//*[@id="o_main_nav"]/ul[2]/li[2]/a/div/sup')
currency_dropdown = (By.CSS_SELECTOR, '[class="dropdown-toggle btn btn-light"]')
currency_select_EUR = (By.CSS_SELECTOR, '[href="/shop/change_pricelist/3"]')
currency_price = (By.XPATH, '//*[@id="product_details"]/form/div/div[1]/div[1]/h3/span[1]')
terms_headline = (By.TAG_NAME, 'h1')
