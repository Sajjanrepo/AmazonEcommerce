import pytest
from pageObjects.ExtractProductsDetails import ProductDetails
from pageObjects.image_Productdescriptions_AddtoCart import Image_ProductDescription_AddtoCart
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_AddToCart:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    test_data = [
        "laptop",  # Test case that should pass
        "19dksdj8u8"  # Test case that should fail
    ]

    @pytest.mark.parametrize("item", test_data)
    def test_add_to_cart(self, setup, item):
        self.logger.info(f"Starting Add to Cart functionality test for item: {item}")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        # Search for the product
        self.logger.info(f"Searching for item: {item}")
        product_page = ProductDetails(self.driver)
        search_result = product_page.search_product(item)

        if search_result:
            self.logger.info(f"Product found for {item}. Fetching details...")
            product_details = product_page.get_product_details()

            if not product_details:
                self.logger.error(f"No product details found for {item}.")
                assert False, f"No product details found for {item}."

            # Test the Add to Cart functionality for the products
            for product in product_details:
                product_link = product["url"]
                self.logger.info(f"Testing Add to Cart for product link: {product_link}")
                self.add_to_cart(product_link, item)

                # Return to the main window
                self.driver.switch_to.window(self.driver.window_handles[0])
        else:
            self.logger.error(f"Search failed. No results found for {item}.")
            assert False, f"Search failed. No results found for {item}."

    def add_to_cart(self, product_link, item):
        # Open the product link in a new tab or window
        self.driver.execute_script(f"window.open('{product_link}', '_blank');")
        new_window = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_window)
        self.logger.info(f"Switched to product page: {product_link}")

        try:
            # Validate the 'Add to Cart' button
            add_to_cart_page = Image_ProductDescription_AddtoCart(self.driver)
            if add_to_cart_page.is_add_to_cart_button_visible(timeout=10):
                self.logger.info(f"'Add to Cart' button is visible for {item}.")
                assert True
            else:
                self.logger.error(f"'Add to Cart' button not found for {item}.")
                assert False, f"'Add to Cart' button not found for {item}."
        finally:
            self.logger.info("Closing product tab.")
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])