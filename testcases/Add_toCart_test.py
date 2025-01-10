import os

import pytest
from pageObjects.ExtractProductsDetails import ProductDetails
from pageObjects.AddToCart import AddToCart
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_AddtoCart:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    test_data = [
        "laptop",  # PASSED
        "19dksdj8u8"  # FAILED
    ]

    @pytest.mark.parametrize("item", test_data)
    def test_add_to_cart(self, setup, item):
        self.logger.info(f"Starting Add to Cart functionality test for item: {item}")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.logger.info(f"Testing item: {item}")
        self.search_item = ProductDetails(self.driver)

        search_res = self.search_item.search_box(item)
        if search_res:
            self.logger.info(f"Product found for {item}")
            self.addcart = AddToCart(self.driver)
            self.productLinks = self.addcart.get_product_links()

            self.logger.info(f"Found {len(self.productLinks)} product links for {item}.")

            if not self.productLinks:
                self.logger.error(f"No product links found for {item}.")
                assert False, f"No product links found for {item}."

            for link in self.productLinks[:2]:
                self.test_add_to_cart_button(link, item)
                self.driver.switch_to.window(self.driver.window_handles[0])

        else:
            self.logger.error(f"Item '{item}' not found.")
            assert False, f"Item '{item}' not found."

    def test_add_to_cart_button(self, link, item):
        main_window = self.driver.current_window_handle
        link.click()
        all_windows = self.driver.window_handles

        for window in all_windows:
            if window != main_window:
                self.driver.switch_to.window(window)
                self.logger.info(f"Switched to window: {window}")

                # Validate the 'Add to Cart' button
                if self.addcart.is_add_to_cart_button_visible(timeout=20):
                    self.logger.info(f"Got the 'Add to Cart' button for {item}.")
                    self.driver.close()
                    assert True
                else:
                    self.logger.error(f"Did not get the 'Add to Cart' button for {item}.")
                    self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + f"screenshot_{item}.png")
                    assert False, f"Add to Cart button not found for {item}."
