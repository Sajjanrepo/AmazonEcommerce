import pytest
from pageObjects.imageanddescriptions import ImageAndDescription
from pageObjects.ExtractProductsDetails import ProductDetails
from pageObjects.AddToCart import AddToCart
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_Image_And_Description:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    test_data = [
        "laptop",  # PASSED
        "MOBILE",  # PASSED
        "6763bhjhdh",  # FAILED
    ]

    @pytest.mark.parametrize("item", test_data)
    def test_image_functionality(self, setup, item):
        self.logger.info(f"Starting image functionality test for item: {item}")
        self.driver = setup

        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.search_item = ProductDetails(self.driver)
        self.search_res = self.search_item.search_box(item)
        if self.search_res:
            self.addcart = AddToCart(self.driver)
            self.productLinks = self.addcart.get_product_links()
            for link in self.productLinks[:2]:
                main_window = self.driver.current_window_handle
                link.click()
                all_windows = self.driver.window_handles

                # Switch to the new window
                for window in all_windows:
                    if window != main_window:
                        self.driver.switch_to.window(window)
                        self.image = ImageAndDescription(self.driver)
                        if self.image.is_image_displayed():
                            self.logger.info("Image functionality validated successfully.")
                            self.driver.close()
                            assert True
                        else:
                            self.logger.error("Image functionality validation failed.")
                            self.driver.close()
                            assert False
                        break
                self.driver.switch_to.window(main_window)
        else:
            self.logger.error(f"Item '{item}' is not available.")
            assert False, f"Item '{item}' is not available."

    @pytest.mark.parametrize("item", test_data)
    def test_productdescription(self, setup, item):
        self.logger.info(f"Starting product description test for item: {item}")
        self.driver = setup

        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.search_item = ProductDetails(self.driver)
        self.search_res = self.search_item.search_box(item)

        if self.search_res:
            self.addcart = AddToCart(self.driver)
            self.productLinks = self.addcart.get_product_links()
            for link in self.productLinks[:2]:
                main_window = self.driver.current_window_handle
                link.click()
                all_windows = self.driver.window_handles

                # Switch to the new window
                for window in all_windows:
                    if window != main_window:
                        self.driver.switch_to.window(window)
                        self.image = ImageAndDescription(self.driver)

                        if self.image.is_product_detail_section_displayed():
                            self.logger.info("Product description validated successfully.")
                            self.driver.close()
                            assert True
                        else:
                            self.logger.error("Product description validation failed.")
                            self.driver.close()
                            assert False
                        break
                self.driver.switch_to.window(main_window)
        else:
            self.logger.error(f"Item '{item}' is not available.")
            assert False, f"Item '{item}' is not available."
