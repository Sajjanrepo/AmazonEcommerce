import pytest
from pageObjects.ExtractProductsDetails import ProductDetails
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_Functional:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    test_data = [
        "laptop",  # This test case should pass
        "MOBILE",  # This test case should pass
        "@123jdhsjsj",  # This test case should fail
        "",            # This test case should fail
        "randomtext",  # This test case should fail
        "<>/1$&#*",  # This test case should fail
        "8573485983"  # This test case should fail
    ]

    @pytest.mark.parametrize("item", test_data)
    def test_search_valid_invalid(self, setup, item):
        self.logger.info(f"Starting test for search item: {item}")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.search_item = ProductDetails(self.driver)
        search_result = self.search_item.search_product(item)

        # Pass when element is found and expected result is SUCCESS
        if search_result:
            self.logger.info("Search succeeded, Expected!")
            assert True, f"Search failed for input '{item}', expected a successful search."
        # Fail when element is NOT found and expected result is ERROR
        else:
            self.logger.error("Search did not succeeded, Expected!")
            assert False
