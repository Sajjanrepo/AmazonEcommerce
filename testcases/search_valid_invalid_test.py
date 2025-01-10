import pytest
from pageObjects.ExtractProductsDetails import ProductDetails
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_Functional:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    test_data = [
        "laptop",  # SUCCESS
        "MOBILE",  # SUCCESS
        "@123jdhsjsj",  # ERROR
        "",            # ERROR
        "randomtext",  # ERROR
        "<>/1$&#*",  # ERROR
        "8573485983"  # ERROR
    ]

    @pytest.mark.parametrize("item", test_data)
    def test_search_valid_invalid(self, setup, item):
        self.logger.info(f"Starting test for search item: {item}")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.search_item = ProductDetails(self.driver)
        self.logger.info(f"Starting test for search item: {item}")
        search_result = self.search_item.search_box(item)

        # Pass when element is found and expected result is SUCCESS
        if search_result:
            assert True, f"Search failed for input '{item}', expected a successful search."
            self.logger.info("Passed: Search succeeded as expected.")

        # Fail when element is NOT found and expected result is ERROR
        else:
            self.logger.error("Passed: Search did not succeeded, Expected!")
            assert False

        self.logger.info(f"Finished test for search item: '{item}'")
