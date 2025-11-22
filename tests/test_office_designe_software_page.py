def test_add_product_to_cart(office_designe):
    office_designe.open_page()
    office_designe.add_to_cart_product()


def test_change_price_currency(office_designe):
    office_designe.open_page()
    office_designe.change_currency()


def test_terms_and_condition_open(office_designe):
    office_designe.open_page()
    office_designe.open_terms_and_conditions()
