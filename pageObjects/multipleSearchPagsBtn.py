from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.customLogger import LogGen


class MultipleSearchBtn:
    NEXT_PAGE_BTN_CSS_SELECTOR = ".s-pagination-next"
    TXT_RESULT_XPATH = "//*[@id='search']/div[1]/div[1]/div/span[1]/div[1]/div[2]/div/span[1]/div/div/h2"

    def __init__(self, driver):
        self.driver = driver
        self.logger = LogGen.loggen()

    def clickNextBtn(self):
        self.driver.find_element(By.CSS_SELECTOR, self.NEXT_PAGE_BTN_CSS_SELECTOR).click()
        try:
            result = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.TXT_RESULT_XPATH))).text
        except Exception as e:
            self.logger.warning(f"Exception occurred: {e}")
            return False

        if result == "Results":
            self.logger.info("Validation passed: Result text matches 'Results'.")
            return True
        else:
            self.logger.warning(f"Validation failed: Expected 'Results', but got '{result}'.")
            return False
