import pytest
from selenium import webdriver
import os
import sys

# Ensure the 'task26' directory is in the Python path
sys.path.append(os.path.abspath('C:\\Users\\VRM\\OneDrive\\Documents\\saucedemo_pom-main\\task26\\pytest.ini'))


@pytest.fixture(scope="function")
def setup(request):
    # Initialize the WebDriver
    driver = webdriver.Chrome()
    driver.get("https://www.imdb.com/search/name/")
    driver.maximize_window()

    # Pass the WebDriver instance to the test class
    request.cls.driver = driver
    yield

    # Close the browser after the test
    driver.quit()
