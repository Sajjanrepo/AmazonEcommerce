import pytest
from pageObjects.image_Productdescriptions_AddtoCart import Image_ProductDescription_AddtoCart
from pageObjects.ExtractProductsDetails import ProductDetails
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_Image_And_Description:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    test_data = [
        "laptop",  # This test case should pass
        "6763bhjhdh",  # This test case should fail
    ]

    @pytest.mark.parametrize("item", test_data)
    def test_image_functionality(self, setup, item):
        self.logger.info(f"Starting image functionality test for item: {item}")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        # Extract product details using the ProductDetails class
        product_page = ProductDetails(self.driver)
        if product_page.search_product(item):
            product_details = product_page.get_product_details()
            if product_details:
                self.logger.info(f"Validating image functionality for {len(product_details)} products.")
                for product in product_details:
                    self.validate_product_image(product["url"])
            else:
                self.logger.warning("No product details found for validation.")
                assert False, "No products found to validate image functionality."
        else:
            self.logger.error(f"Search failed or no results for item '{item}'.")
            assert False, f"Search failed for item '{item}'."

    @pytest.mark.parametrize("item", test_data)
    def test_product_description(self, setup, item):
        self.logger.info(f"Starting product description test for item: {item}")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        # Extract product details using the ProductDetails class
        product_page = ProductDetails(self.driver)
        if product_page.search_product(item):
            product_details = product_page.get_product_details()
            if product_details:
                self.logger.info("Validating product description functionality.")
                for product in product_details:
                    self.validate_product_description(product["url"])
            else:
                self.logger.warning("No product details found for validation.")
                assert False, "No products found to validate description functionality."
        else:
            self.logger.error(f"Search failed or no results for item '{item}'.")
            assert False, f"Search failed for item '{item}'."

    def validate_product_image(self, product_url):
        self.logger.info(f"Validating image functionality for product URL: {product_url}")
        main_window = self.driver.current_window_handle
        self.driver.execute_script("window.open(arguments[0]);", product_url)
        all_windows = self.driver.window_handles

        for window in all_windows:
            if window != main_window:
                self.driver.switch_to.window(window)
                try:
                    image_check = Image_ProductDescription_AddtoCart(self.driver)
                    assert image_check.is_image_displayed(), "Image is not visible for the product."
                    self.logger.info("Image functionality validated successfully.")
                except Exception as e:
                    self.logger.error(f"Image validation failed: {e}")
                    assert False, "Image validation failed."
                finally:
                    self.driver.close()
                    self.driver.switch_to.window(main_window)

    def validate_product_description(self, product_url):
        self.logger.info(f"Validating description functionality for product URL: {product_url}")
        main_window = self.driver.current_window_handle
        self.driver.execute_script("window.open(arguments[0]);", product_url)
        all_windows = self.driver.window_handles

        for window in all_windows:
            if window != main_window:
                self.driver.switch_to.window(window)
                try:
                    description_check = Image_ProductDescription_AddtoCart(self.driver)
                    assert description_check.is_product_detail_section_displayed(), "Product description is not visible."
                    self.logger.info("Product description validated successfully.")
                except Exception as e:
                    self.logger.error(f"Description validation failed: {e}")
                    assert False, "Description validation failed."
                finally:
                    self.driver.close()
                    self.driver.switch_to.window(main_window)
