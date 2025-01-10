from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.customLogger import LogGen


class ImageAndDescription:
    def __init__(self, driver):
        self.driver = driver
        self.product_description_id = "productOverview_feature_div"
        self.image_functionality_id = "altImages"
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
