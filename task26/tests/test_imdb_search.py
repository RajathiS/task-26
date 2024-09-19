import pytest
from selenium import webdriver
from pages.imdb_search_page import IMDbSearchPage  # Make sure the path to the POM file is correct


@pytest.fixture
def driver():
    driver = webdriver.Chrome()  # Or the appropriate WebDriver for your browser
    yield driver
    driver.quit()


def test_imdb_search(driver):
    imdb_page = IMDbSearchPage(driver)

    # Open the IMDb search page
    imdb_page.open()

    # Fill in the details
    imdb_page.fill_name("Tom Hanks")
    imdb_page.select_gender("Male")
    imdb_page.select_birth_month("July")
    imdb_page.fill_birth_year("1956")
    imdb_page.select_sort("Popularity")

    # Perform the search
    imdb_page.click_search()

    # Verify that the results page has loaded
    assert "Tom Hanks" in driver.title
