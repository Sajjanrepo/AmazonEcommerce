from pageObjects.ExtractProductsDetails import ProductDetails
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class TestScreenSizes:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()
    item = "mobile"  # Test case that should pass

    def setup_test_environment(self, setup, width, height):
        self.logger.info("Starting Responsiveness test for Amazon Website")
        self.logger.info(f"Initializing test for screen size: {width}x{height}")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.set_window_size(width, height)
        self.logger.info(f"Screen size set to {width}x{height}")

    # Performing Search operation for different screen sizes
    def perform_search_and_validate(self):
        # Search for the product
        self.logger.info(f"Searching for item: {self.item}")
        product_page = ProductDetails(self.driver)
        if product_page.search_product(self.item):
            self.logger.info("Search completed successfully.")
            product_details = product_page.get_product_details()

            if not product_details:
                self.logger.error("No products found in the search results.")
                return False

            # Printing the product names
            for product in product_details:
                product_name = product.get('name', '')
                if product_name:
                    self.logger.info(f"Product found: {product_name}")
                else:
                    self.logger.error("A product in the list has an empty name.")
                    return False
            return True
        else:
            self.logger.error(f"No results found for the search item: {self.item}")
            return False

    def run_test_for_screen_size(self, setup, width, height):
        try:
            self.setup_test_environment(setup, width, height)
            if self.perform_search_and_validate():
                self.logger.info(f"Test PASSED for screen size: {width}x{height}")
            else:
                self.logger.error(f"Test FAILED for screen size: {width}x{height}")
                assert False
        except Exception as e:
            self.logger.error(f"An error occurred during the test: {str(e)}")
            assert False

    def test_screen_sizes(self, setup):
        screen_sizes = [(1920, 1080), (768, 1030), (360, 700)]
        for width, height in screen_sizes:
            self.logger.info(f"Starting test for screen size: {width}x{height}")
            self.run_test_for_screen_size(setup, width, height)
