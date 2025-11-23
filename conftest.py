import pytest
from selenium import webdriver

from pages.cart_page import CartPage
from pages.multimedia_category_products_page import OfficeDesigne
from pages.section_desc_page import Section_Desc_Page


@pytest.fixture
def driver():
    chrome_driver = webdriver.Chrome()
    return chrome_driver


@pytest.fixture()
def section_desc(driver):
    return Section_Desc_Page(driver)


@pytest.fixture()
def cart_page(driver):
    return CartPage(driver)


@pytest.fixture()
def office_designe(driver):
    return OfficeDesigne(driver)
