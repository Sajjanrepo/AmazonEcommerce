from pageObjects.ExtractProductsDetails import ProductDetails
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_DifferentScreenSize:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()
    item = "mobile"  # PASSED

    def setup_test_environment(self, setup, width, height):
        self.logger.info(f"Starting screen size functionality test for width: {width} , height : {height}")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.set_window_size(width, height)
        self.logger.info("Screen size set to: %sx%s", width, height)

    def perform_search_and_validate(self):
        self.search_item = ProductDetails(self.driver)
        if self.search_item.search_box(self.item):
            self.productName = self.search_item.getProductName()
            if len(self.productName) > 0:
                self.logger.info(f"The product names are: {self.productName}")
                return True
            else:
                self.logger.error("Product Name list is empty")
                return False
        else:
            self.logger.error(f"Search item '{self.item}' is not available")
            return False

    def run_test_for_screen_size(self, setup, width, height):
        try:
            self.setup_test_environment(setup, width, height)
            result = self.perform_search_and_validate()
            assert result, f"Test failed for screen size {width}x{height}"
            self.logger.info("Test PASSED for screen size: %sx%s", width, height)
        except AssertionError as e:
            self.logger.error("Test FAILED for screen size: %sx%s - %s", width, height, str(e))
            assert False

    def test_screen_sizes(self, setup):
        screen_sizes = [(1920, 1080), (768, 1030), (360, 700)]
        for width, height in screen_sizes:
            self.run_test_for_screen_size(setup, width, height)
