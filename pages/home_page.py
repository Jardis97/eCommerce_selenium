# home_page.py eredita da base_page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class HomePage(BasePage):
    url = "http://automationexercise.com" #url home page
    cookies_consent = "//p[text()='Consent']"
    logo_visibility = "//img[@alt='Website for automation practice']"

    def __init__(self, driver):
        super().__init__(driver)

    def load_homepage(self):
        self.driver.get(self.url)

    def homepage_visibility(self):
        logo_visibility = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.logo_visibility)))



