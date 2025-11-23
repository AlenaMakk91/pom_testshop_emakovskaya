def test_empty_cart_message(cart_page):
    cart_page.open_page()
    cart_page.empty_cart_message()


def test_check_total_price_if_product_qnty_changed(cart_page, office_designe):
    office_designe.open_page()
    office_designe.add_product_to_cart()
    cart_page.open_page()
    cart_page.change_product_quantity_and_verify_total_price()


def test_check_invalid_promo(cart_page, office_designe):
    office_designe.open_page()
    office_designe.add_product_to_cart()
    cart_page.open_page()
    cart_page.check_invalid_promo()
