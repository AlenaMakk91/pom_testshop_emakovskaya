def test_empty_cart_message(cart_page):
    cart_page.open_page()
    cart_page.empty_cart_message()


def test_change_product_quantity(cart_page, office_designe):
    office_designe.open_page()
    office_designe.get_product_in_cart()
    cart_page.open_page()
    cart_page.change_product_quantity()


def test_check_invalid_promo(cart_page, office_designe):
    office_designe.open_page()
    office_designe.get_product_in_cart()
    cart_page.open_page()
    cart_page.check_invalid_promo()
