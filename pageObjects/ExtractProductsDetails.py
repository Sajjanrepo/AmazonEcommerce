from utilities.customLogger import LogGen
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductDetails:
    searchbox_xpath = "//input[@id='twotabsearchtextbox']"
    lnk_product_xpath = "//div[@role='listitem']/div/div/span/div/div/div//div[@class='puisg-col-inner']//div[@data-cy='title-recipe']/a"
    product_name_xpath = "//div[@role='listitem']/div/div/span/div/div/div//div[@class='puisg-col-inner']//div[@data-cy='title-recipe']//h2/span"
    ratings_xpath = "//div[@role='listitem']/div/div/span/div/div/div/div[2]/div/div/div[2]/div[1]/span/a/i[1]/span"
    price_xpath = "//div[@role='listitem']/div/div/span/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div/div[1]/a/span/span[2]/span[2]"
    search_btn_xpath = "//input[@id='nav-search-submit-button']"
    txt_result_xpath = "//*[@id='search']/div[1]/div[1]/div/span[1]/div[1]/div[2]/div/span[1]/div/div/h2"
    back_to_result_xpath = "//*[@id='breadcrumb-back-link']"

    def __init__(self, driver):
        self.driver = driver
        self.logger = LogGen.loggen()

    def search_box(self, item):
        self.logger.info(f"Searching for item: {item}")
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

    def getProductName(self):
        productname_list = []
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, self.product_name_xpath))
            )
            self.productname = self.driver.find_elements(By.XPATH, self.product_name_xpath)
            if not self.productname:
                self.logger.warning("No product names found.")
            for name in self.productname:
                productname_list.append(name.text)
            self.logger.info(f"Product names extracted: {len(productname_list)}")
            self.logger.debug(f"Extracted Product Names: {productname_list}")
        except Exception as e:
            self.logger.error(f"Error extracting product names: {e}")
        return productname_list

    def getProductPrice(self):
        productprice_list = []
        try:
            self.productPrice = self.driver.find_elements(By.XPATH, self.price_xpath)
            if not self.productPrice:
                self.logger.warning("No product prices found.")
            for price in self.productPrice:
                productprice_list.append(price.text)
            self.logger.info(f"Product prices extracted: {len(productprice_list)}")
        except Exception as e:
            self.logger.error(f"Error extracting product prices: {e}")
        return productprice_list

    def getProductRating(self):
        productrating_list = []
        try:
            self.productRating = self.driver.find_elements(By.XPATH, self.ratings_xpath)
            if not self.productRating:
                self.logger.warning("No product ratings found.")
            for rating in self.productRating:
                productrating_list.append(rating.get_attribute("innerHTML"))
            self.logger.info(f"Product ratings extracted: {len(productrating_list)}")
        except Exception as e:
            self.logger.error(f"Error extracting product ratings: {e}")
        return productrating_list

    def getProductURL(self):
        product_url = []
        try:
            productLink = self.driver.find_elements(By.XPATH, self.lnk_product_xpath)
            if not productLink:
                self.logger.warning("No product links found.")
            for link in productLink:
                product_url.append(link.get_attribute("href"))
            self.logger.info(f"Product URLs extracted: {len(product_url)}")
        except Exception as e:
            self.logger.error(f"Error extracting product URLs: {e}")
        return product_url
