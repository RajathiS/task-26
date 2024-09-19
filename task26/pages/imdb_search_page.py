from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class IMDbSearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://www.imdb.com/search/name/"

    def open(self):
        self.driver.get(self.base_url)

    def fill_name(self, name):
        name_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "name"))
        )
        name_field.clear()
        name_field.send_keys(name)

    def select_gender(self, gender):
        gender_dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "gender"))
        )
        gender_dropdown.send_keys(gender)

    def select_birth_month(self, month):
        month_dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "birth_month"))
        )
        month_dropdown.send_keys(month)

    def fill_birth_year(self, year):
        year_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "birth_year"))
        )
        year_field.clear()
        year_field.send_keys(year)

    def select_sort(self, sort_option):
        sort_dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "sort"))
        )
        sort_dropdown.send_keys(sort_option)

    def click_search(self):
        search_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        )
        search_button.click()
