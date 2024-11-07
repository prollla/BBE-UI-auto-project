from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from bbe.pages.base_page import BasePage


class CartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def delete_product_locator(self):
        return By.CSS_SELECTOR, 'button.button.js-item-delete'


    def empty_cart_locator(self):
        return By.CSS_SELECTOR, 'div.js-cart-empty'

    def delete_product_from_cart(self):
        self.click(self.delete_product_locator())

    def find_empty_cart_element(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.empty_cart_locator()))
        return self.find(self.empty_cart_locator())

