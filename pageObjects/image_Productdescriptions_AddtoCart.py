from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.customLogger import LogGen


class Image_ProductDescription_AddtoCart:
    Add_to_cart_xpath = "//*[@id='submit.add-to-cart-announce']"
    image_functionality_id = "altImages"
    product_description_id = "productOverview_feature_div"

    def __init__(self, driver):
        self.driver = driver
        self.logger = LogGen.loggen()

    def is_element_displayed(self, by_locator):

        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))
            return element.is_displayed()
        except TimeoutError:
            self.logger.error(f"Element with locator {by_locator} not found within the timeout period.")
            return False

    def is_image_displayed(self):
        result = self.is_element_displayed((By.ID, self.image_functionality_id))
        if result:
            self.logger.info("Product image functionality is displayed.")
        else:
            self.logger.warning("Product image functionality is NOT displayed.")
        return result

    def is_product_detail_section_displayed(self):
        result = self.is_element_displayed((By.ID, self.product_description_id))
        if result:
            self.logger.info("Product detail section is displayed.")
        else:
            self.logger.warning("Product detail section is NOT displayed.")
        return result

    def is_add_to_cart_button_visible(self, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, self.Add_to_cart_xpath))
            )
            add_to_cart_button = self.driver.find_element(By.XPATH, self.Add_to_cart_xpath)
            if add_to_cart_button.is_displayed():
                self.logger.info("'Add to Cart' button is visible.")
                return True
            else:
                self.logger.warning("'Add to Cart' button is not visible.")
                return False
        except TimeoutError:
            self.logger.error("Timeout while waiting for 'Add to Cart' button to appear.")
            return False