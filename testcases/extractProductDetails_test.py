import csv
import pytest
from pageObjects.ExtractProductsDetails import ProductDetails
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_Crawling:
    baseURL = ReadConfig.getApplicationURL()
    csv_path = ReadConfig.getCSV_Path()
    logger = LogGen.loggen()
    logger.info(f"Starting the Product Details Extraction Test case")

    test_data = [
        "mobile",  # This test case should pass
        "jhdsdjbd76373"  # This test case should fail
    ]

    @pytest.mark.parametrize("item", test_data)
    def test_search(self, setup, item):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        search_item = ProductDetails(self.driver)
        if search_item.search_product(item):
            return search_item
        else:
            self.logger.error(f"Search item '{item}' is not available")
            assert False, f"Search item '{item}' is not available.EXPECTED TO FAIL"

    def extract_product_details(self, setup, item):

        # Extract product details using the ProductDetails class
        search_item = self.test_search(setup, item)
        product_details = search_item.get_product_details()

        self.logger.info(f"Printing the Name, Price , Rating , URL for {item}")
        for product in product_details:
            self.logger.info(f"Product Name: {product['name']}")
            self.logger.info(f"Product Price: {product['price']}")
            self.logger.info(f"Product Rating: {product['rating']}")
            self.logger.info(f"Product URL: {product['url']}")

        # Validate that product details were extracted
        assert len(product_details) > 0, "No products extracted! FAILED: EXPECTED list of products"
        return product_details

    @pytest.mark.parametrize("item", test_data)
    def test_WriteToCSV(self, setup, item):
        # Extract product details for the given item
        product_details = self.extract_product_details(setup, item)

        # Write to CSV
        with open(self.csv_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Price', 'Rating', 'URL'])

            for product in product_details:
                writer.writerow([product['name'], product['price'], product['rating'], product['url']])

        self.logger.info(f"Extracted {len(product_details)} products to CSV.")
        assert len(product_details) > 0, "No products extracted! FAILED: EXPECTED list of products"
