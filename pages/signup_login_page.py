# base_page.py servirà per le azioni comune nelle pagine tipo
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SignLogPage:

    def __init__(self, driver):
        """Passo il driver al momento della creazione della classe da browserInstance in conftest"""
        self.driver = driver
        self.usersignup_visibility = "//h2[text()='New User Signup!!']"


    def newUserSignup_visibility(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.usersignup_visibility))
        ).click()

#
# 4. Click on 'Signup / Login' button
# 5. Verify 'New User Signup!' is visible
# 6. Enter name and email address