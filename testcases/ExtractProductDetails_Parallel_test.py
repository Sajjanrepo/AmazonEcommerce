import pytest
from pageObjects.ExtractProductsDetails import ProductDetails
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_Crawling_Parallel:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    test_data = [
        "laptop",  # PASSED
        "@#$^!123hss"  # FAILED
    ]

    @pytest.mark.parametrize("item", test_data)
    def test_search_parallel(self, setup, item):
        self.logger.info(f"Parallel Testing for Product Details Extraction functionality using Selenium Grid")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        search_item = ProductDetails(self.driver)
        if search_item.search_box(item):
            self.logger.info(f"Showing the results for product '{item}'")
            return search_item
        else:
            self.logger.error(f"FAIL:Search item '{item}' is not available, Expected")
            assert False, f"Search item '{item}' is not available"

    @pytest.mark.parametrize("item", test_data)
    def test_productName_parallel(self, setup, item):
        self.search_item = self.test_search_parallel(setup, item)
        self.product_name = self.search_item.getProductName()

        if len(self.product_name) > 0:
            self.logger.info(f"Extracted Product Names: {self.product_name}")
            assert True
        else:
            self.logger.error("FAIL:No product names extracted!")
            assert False

    @pytest.mark.parametrize("item", test_data)
    def test_productPrice_parallel(self, setup, item):
        self.search_item = self.test_search_parallel(setup, item)
        self.product_price = self.search_item.getProductPrice()

        if len(self.product_price) > 0:
            self.logger.info(f"Extracted Product Prices: {self.product_price}")
            assert True
        else:
            self.logger.error("FAIL:No product prices extracted!")
            assert False

    @pytest.mark.parametrize("item", test_data)
    def test_productRating_parallel(self, setup, item):
        self.search_item = self.test_search_parallel(setup, item)
        self.product_rating = self.search_item.getProductRating()

        if len(self.product_rating) > 0:
            self.logger.info(f"Extracted Product Ratings: {self.product_rating}")
            assert True
        else:
            self.logger.error("FAIL:No product ratings extracted!")
            assert False

    @pytest.mark.parametrize("item", test_data)
    def test_ProductURL_parallel(self, setup, item):
        self.search_item = self.test_search_parallel(setup, item)
        self.url_list = self.search_item.getProductURL()

        if len(self.url_list) > 0:
            self.logger.info(f"Extracted Product URLs: {self.url_list}")
            assert True
        else:
            self.logger.error("FAIL:No product URLs extracted!")
