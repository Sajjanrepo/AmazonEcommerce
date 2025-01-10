import os
import pytest
from selenium import webdriver
from datetime import datetime
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


@pytest.fixture(scope="session")
def setup(browser):
    driver = None
    logger = LogGen.loggen()

    # Setup browser
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
    options = None

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        return webdriver.Remote(command_executor="http://192.168.1.20:4444/wd/hub", options=options)

    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.binary_location = ReadConfig.getFirefoxPath()
        return webdriver.Remote(command_executor="http://192.168.1.20:4444/wd/hub", options=options)

    elif browser == "edge":
        options = webdriver.EdgeOptions()
        return webdriver.Remote(command_executor="http://192.168.1.20:4444/wd/hub", options=options)

    logger.error("Invalid browser name. Please provide 'chrome', 'firefox', or 'edge'")
    return None


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


# Configure reports with timestamp and create reports directory if it doesn't exist
@pytest.hookimpl(optionalhook=True)
def pytest_configure(config):
    test_file_name = os.path.splitext(os.path.basename(config.args[0]))[0]
    report_dir = os.path.abspath(os.curdir) + "\\reports\\"
    os.makedirs(report_dir, exist_ok=True)
    report_filename = test_file_name + " - " + datetime.now().strftime("%d-%m-%Y %H-%M-%S") + ".html"
    config.option.htmlpath = report_dir + report_filename
