import csv
import pytest

from pageObjects.ExtractProductsDetails import ProductDetails
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_Crawling:
    baseURL = ReadConfig.getApplicationURL()
    csv_path = ReadConfig.getCSV_Path()
    logger = LogGen.loggen()

    test_data = [
        "mobile",  # PASSED
        "jhdsdjbd76373"  # FAILED
    ]

    @pytest.mark.parametrize("item", test_data)
    def test_search(self, setup, item):
        self.logger.info(f"Starting the Product Details Extraction Functionality Test case")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        search_item = ProductDetails(self.driver)
        if search_item.search_box(item):
            self.logger.info(f"Showing the results for product '{item}'")
            return search_item
        else:
            self.logger.error(f"Search item '{item}' is not available")
            assert False, f"Search item '{item}' is not available"

    @pytest.mark.parametrize("item", test_data)
    def test_productName(self, setup, item):
        self.search_item = self.test_search(setup, item)
        self.product_name = self.search_item.getProductName()

        if len(self.product_name) > 0:
            self.logger.info(f"Extracted Product Names: {self.product_name}")
            assert True
            return self.product_name
        else:
            self.logger.error("FAIL:No product names extracted!")
            assert False

    @pytest.mark.parametrize("item", test_data)
    def test_productPrice(self, setup, item):
        self.search_item = self.test_search(setup, item)
        self.product_price = self.search_item.getProductPrice()

        if len(self.product_price) > 0:
            self.logger.info(f"Extracted Product Prices: {self.product_price}")
            assert True
            return self.product_price
        else:
            self.logger.error("FAIL:No product prices extracted!")
            assert False

    @pytest.mark.parametrize("item", test_data)
    def test_productRating(self, setup, item):
        self.search_item = self.test_search(setup, item)
        self.product_rating = self.search_item.getProductRating()

        if len(self.product_rating) > 0:
            self.logger.info(f"Extracted Product Ratings: {self.product_rating}")
            assert True
            return self.product_rating
        else:
            self.logger.error("FAIL:No product ratings extracted!")
            assert False

    @pytest.mark.parametrize("item", test_data)
    def test_ProductURL(self, setup, item):
        self.search_item = self.test_search(setup, item)
        self.url_list = self.search_item.getProductURL()

        if len(self.url_list) > 0:
            self.logger.info(f"Extracted Product URLs: {self.url_list}")
            assert True
            return self.url_list
        else:
            self.logger.error("FAIL:No product URLs extracted!")

    @pytest.mark.parametrize("item", test_data)
    def test_WriteToCSV(self, setup, item):

        # Extract product details
        self.product_name = self.test_productName(setup, item)
        self.product_price = self.test_productPrice(setup, item)
        self.product_rating = self.test_productRating(setup, item)
        self.url_list = self.test_ProductURL(setup, item)

        products = []
        for indx in range(len(self.product_name)):
            name = self.product_name[indx]
            price = self.product_price[indx]
            rating = self.product_rating[indx]
            url = self.url_list[indx]
            products.append([name, price, rating, url])

        # Write to CSV
        with open(self.csv_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Price', 'Rating', 'URL'])
            writer.writerows(products)

        self.logger.info(f"Extracted {len(products)} products to CSV.")
        assert len(products) > 0, "No products extracted!"
