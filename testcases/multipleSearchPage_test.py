from pageObjects.ExtractProductsDetails import ProductDetails
from pageObjects.multipleSearchPagsBtn import MultipleSearchBtn
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class TestMultipleSearchPage:
    base_url = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    item = "Mobile"  # This test case should pass

    def test_click_next_btn(self, setup):
        self.logger.info("Starting Test: Multiple Search Page")
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()

        try:
            # Extract product details using the ProductDetails class
            self.search_item = ProductDetails(self.driver)
            if not self.search_item.search_product(self.item):
                self.logger.error(f"Search failed: Item '{self.item}' is not available.")
                assert False, "Search item is not available."

            self.logger.info(f"Results displayed for product: {self.item}")
            self.product_list = self.search_item.get_product_details()
            for product in self.product_list:
                product_name = product["name"]
                self.logger.info(f"Product Name: {product_name}")

            self.multiple_search_page = MultipleSearchBtn(self.driver)
            test_result = self.multiple_search_page.clickNextBtn()

            if test_result:
                self.logger.info("Next button functionality validated successfully.")
                assert True
            else:
                self.logger.error(f"Next button validation failed")
                assert False

        except Exception as e:
            self.logger.error(f"Test encountered an exception: {e}")
            assert False, f"Test failed due to exception: {e}"

