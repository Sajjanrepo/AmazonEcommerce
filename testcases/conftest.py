import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from selenium.webdriver.firefox.options import Options


@pytest.fixture(scope="session")
def setup(browser):
    logger = LogGen.loggen()

    driver = get_driver(browser, logger)

    if driver:
        logger.info(f"Launching {browser} Browser")
    else:
        logger.error(f"Invalid browser name {browser} provided")

    yield driver

    # Close the driver after test session ends
    if driver:
        logger.info(f"Closing {browser} Browser")
        driver.quit()


def get_driver(browser, logger):
    if browser == "chrome":
        chrome_driver_path = ReadConfig.getchromedriver()
        options = webdriver.ChromeOptions()

        # Create the Service object with the ChromeDriver path
        serv_obj = Service(executable_path=chrome_driver_path)

        # Initialize the ChromeDriver
        driver = webdriver.Chrome(service=serv_obj, options=options)
        return driver

        # For parallel run on Selenium Grid
        # options = webdriver.ChromeOptions()
        # options.binary_location=ReadConfig.getChromePath()
        # return webdriver.Remote(command_executor="http://192.168.1.5:4444/wd/hub", options=options)

    elif browser == "firefox":
        firefox_driver_path = ReadConfig.getFirefoxdriver()
        options = Options()
        options.binary_location = ReadConfig.getFirefoxPath()
        serv_obj = Service(executable_path=firefox_driver_path)
        driver = webdriver.Firefox(service=serv_obj, options=options)
        return driver

        # For parallel run on Selenium Grid
        # options = webdriver.FirefoxOptions()
        # options.binary_location = ReadConfig.getFirefoxPath()
        # return webdriver.Remote(command_executor="http://192.168.1.5:4444/wd/hub", options=options)

    logger.error("Invalid browser name. Please provide 'chrome', 'firefox'")
    return None


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


# Configure reports with timestamp and create reports directory if it doesn't exist
@pytest.hookimpl(optionalhook=True)
def pytest_configure(config):
    import os
    from datetime import datetime

    # Get the test file name from the command-line arguments
    if config.args:
        test_file_name = os.path.splitext(os.path.basename(config.args[0]))[0]
    else:
        test_file_name = "test_report"  # Default name if no specific file is passed

    report_dir = os.path.abspath(os.curdir) + "\\reports\\"
    os.makedirs(report_dir, exist_ok=True)

    # Generate the report filename with timestamp
    report_filename = f"{test_file_name} - {datetime.now().strftime('%d-%m-%Y %H-%M-%S')}.html"

    # Ensure the HTML report path is set correctly
    html_path = os.path.join(report_dir, report_filename)
    config.option.htmlpath = html_path
