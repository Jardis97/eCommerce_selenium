# base_page.py servirà per le azioni comune nelle pagine tipo
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class SignLogPage:

    def __init__(self, driver):
        """Passo il driver al momento della creazione della classe da browserInstance in conftest"""
        self.driver = driver
        self.usersignup_visibility = "//h2[text()='New User Signup!']"
        self.enterName = "input[data-qa='signup-name']"
        self.enterEmail = "input[data-qa='signup-email']"
        self.signupButton = "button[data-qa='signup-button']"
        self.textaccount_visibility = "//h2[@class='title text-center']/b[text()='Enter Account Information']"
        #Parametri per il signup
        self.Mr = "id_gender1"
        self.Name = "name"
        self.Email = "email"
        self.Password = "password"
        self.DateofBirth= {
            "day": "days",
            "month": "months",
            "year": "years"
        }
        self.Checkbox_newsletter = "newsletter"

        self.address = {
            "first_name" : "first_name",
            "last_name" : "last_name",
            "address" : "address1",
            "state" : "state",
            "city": "city",
            "zipcode" : "zipcode",
            "mobile_number": "mobile_number",
        }

        self.createButton = "button[data-qa='create-account']"
        self.accountCreatedVis = "h2[data-qa='account-created']"

    #funzione per verificare che ci sia la scritta visibile
    def newUserSignup_visibility(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.usersignup_visibility))
        ).click()

    #funzione per inserire nome e email
    def enterName_email(self, name_value, email_value): #i due campi verranno popolati da test_RegisterUser
        name = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.enterName)))
        name.send_keys(name_value)
        email = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.enterEmail)))
        email.send_keys(email_value)

    #funzione per cliccare su bottone signup
    def signup_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.signupButton))
        ).click()
    #verifica sia visibile post signup
    def accountinfo_visibility(self):
        text_visibility = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.textaccount_visibility)))
        return text_visibility

    def fill_details(self, name_value, email_value, password_value, day_value,
                     month_value, year_value, firstName_value, lastName_value, address_value,
                     state_value, city_value, zipcode_value, mobileNumber_value):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, self.Mr))).send_keys(name_value)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, self.Name))).send_keys(email_value)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, self.Password))).send_keys(password_value)

        #Fill date of birth
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, self.DateofBirth["day"]))).send_keys(day_value)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, self.DateofBirth["month"]))).send_keys(month_value)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, self.DateofBirth["year"]))).send_keys(year_value)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, self.Checkbox_newsletter))).click()
        #Da ora in poi per evitare ripetizioni di codice userò funzinoe Webdriverwait dichiarata in base_page
        base_page = BasePage(self.driver)
        base_page.wait_and_fill(By.ID, self.address["first_name"], firstName_value)
        base_page.wait_and_fill(By.ID, self.address["last_name"], lastName_value)
        base_page.wait_and_fill(By.ID, self.address["address"], address_value)
        base_page.wait_and_fill(By.ID, self.address["state"], state_value)
        base_page.wait_and_fill(By.ID, self.address["city"], city_value)
        base_page.wait_and_fill(By.ID, self.address["zipcode"], zipcode_value)
        base_page.wait_and_fill(By.ID, self.address["mobile_number"], mobileNumber_value)
        #Clicco su Create Account
        base_page.wait_and_click(By.CSS_SELECTOR, self.createButton)


    def account_created_vis(self):
        avisibility = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.accountCreatedVis)))
        return avisibility

