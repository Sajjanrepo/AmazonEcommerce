from pageObjects.ExtractProductsDetails import ProductDetails
from pageObjects.multipleSearchPagsBtn import MultipleSearchBtn
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class TestMultipleSearchPage:
    base_url = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    item = "Mobile"  # PASSED

    def test_click_next_btn(self, setup):
        self.logger.info("***** Starting Test: Multiple Search Page *****")
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()

        try:
            self.search_item = ProductDetails(self.driver)
            if not self.search_item.search_box(self.item):
                self.logger.error(f"Search failed: Item '{self.item}' is not available.")
                assert False, "Search item is not available."

            self.logger.info(f"Results displayed for product: {self.item}")
            self.product_list = self.search_item.getProductName()
            self.logger.info(f"Product list for '{self.item}': {self.product_list}")

            self.multiple_search_page = MultipleSearchBtn(self.driver)
            test_result = self.multiple_search_page.clickNextBtn()

            if test_result:
                self.logger.info("Next button functionality validated successfully.")
                self.logger.info(f"Test Passed")
                assert True
            else:
                self.logger.error(f"Next button validation failed")
                assert False

        except Exception as e:
            self.logger.error(f"Test encountered an exception: {e}")
            assert False, f"Test failed due to exception: {e}"

        finally:
            self.logger.info("***** Ending Test: Multiple Search Page *****")
