from utilities.customLogger import LogGen
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductDetails:
    homepage_url = "https://www.amazon.in"
    searchbox_xpath = "//input[@id='twotabsearchtextbox']"
    search_btn_xpath = "//input[@id='nav-search-submit-button']"
    product_name_xpath = "//div[@role='listitem']/div/div/span/div/div/div//div[@class='puisg-col-inner']//div[@data-cy='title-recipe']//h2/span"
    price_xpath = "//div[@role='listitem']/div/div/span/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div/div[1]/a/span/span[2]/span[2]"
    ratings_xpath = "//div[@role='listitem']/div/div/span/div/div/div/div[2]/div/div/div[2]/div[1]/span/a/i[1]/span"
    lnk_product_xpath = "//div[@role='listitem']/div/div/span/div/div/div//div[@class='puisg-col-inner']//div[@data-cy='title-recipe']/a"
    txt_result_xpath = "//*[@id='search']/div[1]/div[1]/div/span[1]/div[1]/div[2]/div/span[1]/div/div/h2"

    def __init__(self, driver):
        self.driver = driver
        self.logger = LogGen.loggen()

    def search_product(self, item):
        self.logger.info(f"Searching for product: {item}")
        self.driver.find_element(By.XPATH, self.searchbox_xpath).clear()
        self.driver.find_element(By.XPATH, self.searchbox_xpath).send_keys(item)
        self.driver.find_element(By.XPATH, self.search_btn_xpath).click()

        try:
            result = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.txt_result_xpath))).text
            if result == "Results":
                self.logger.info("Search was successful.")
                return True
            else:
                self.logger.error("Search did not return expected results.")
                return False
        except Exception as e:
            self.logger.error(f"Error during search: {e}")
            return False

    def get_product_details(self):
        product_details = []
        try:
            product_names = self.driver.find_elements(By.XPATH, self.product_name_xpath)
            product_prices = self.driver.find_elements(By.XPATH, self.price_xpath)
            product_ratings = self.driver.find_elements(By.XPATH, self.ratings_xpath)
            product_links = self.driver.find_elements(By.XPATH, self.lnk_product_xpath)

            if len(product_names) == 0:
                self.logger.warning("No product names found.")
            if len(product_prices) == 0:
                self.logger.warning("No product prices found.")
            if len(product_ratings) == 0:
                self.logger.warning("No product ratings found.")
            if len(product_links) == 0:
                self.logger.warning("No product links found.")

            for name, price, rating, link in zip(product_names, product_prices, product_ratings, product_links):
                product_details.append({
                    "name": name.text.strip(),
                    "price": price.text.strip(),
                    "rating": rating.get_attribute("innerHTML").strip(),
                    "url": link.get_attribute("href")
                })

            self.logger.info(f"Extracted details for {len(product_details)} products.")
            self.logger.debug(f"Extracted Product Details: {product_details}")
        except Exception as e:
            self.logger.error(f"Error extracting product details: {e}")

        return product_details
