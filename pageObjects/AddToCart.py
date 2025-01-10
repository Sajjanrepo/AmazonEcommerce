from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utilities.customLogger import LogGen


class AddToCart:

    # Locators
    ADD_TO_CART_BUTTON_XPATH = "//*[@id='submit.add-to-cart-announce']"
    PRODUCT_LINKS_XPATH = (
        "//div[@role='listitem']/div/div/span/div/div/div//div[@class='puisg-col-inner']//div["
        "@data-cy='title-recipe']/a"
    )

    logger = LogGen.loggen()

    def __init__(self, driver):
        self.driver = driver

    def is_add_to_cart_button_visible(self, timeout=20):

        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, self.ADD_TO_CART_BUTTON_XPATH))
            )
            add_to_cart_button = self.driver.find_element(By.XPATH, self.ADD_TO_CART_BUTTON_XPATH)
            if add_to_cart_button.is_displayed():
                self.logger.info("PASS: 'Add to Cart' button is visible.")
                return True
            else:
                self.logger.warning("FAIL: 'Add to Cart' button is not visible.")
                return False
        except TimeoutException:
            self.logger.error("FAIL: Timeout while waiting for 'Add to Cart' button to appear.")
            return False

    def get_product_links(self):

        try:
            product_links = self.driver.find_elements(By.XPATH, self.PRODUCT_LINKS_XPATH)
            if product_links:
                self.logger.info(f"PASS: Found {len(product_links)} product links.")
            else:
                self.logger.warning("FAIL: No product links found.")
            return product_links
        except Exception as e:
            self.logger.error(f"FAIL: Error while retrieving product links: {e}")
            return []

