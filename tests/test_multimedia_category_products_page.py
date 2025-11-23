def test_add_product_to_cart_and_verify(office_designe):
    office_designe.open_page()
    office_designe.add_product_to_cart_and_verify()


def test_change_price_currency(office_designe):
    office_designe.open_page()
    office_designe.change_currency_to_eur_and_verify()


def test_terms_and_condition_open(office_designe):
    text = 'STANDARD TERMS AND CONDITIONS OF SALE'
    office_designe.open_page()
    office_designe.open_terms_and_conditions(text)
