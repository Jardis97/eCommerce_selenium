# base_page.py servirà per le azioni comune nelle pagine tipo
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        """Passo il driver al momento della creazione della classe da browserInstance in conftest"""
        self.driver = driver
        self.cookies_consent = "//p[text()='Acconsento']"
        self.login_button = "a[href='/login']"



    def click(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator)).click()

    def accept_cookies(self):
        # Attendi che l'elemento "Consent" diventi cliccabile (fino a 10 secondi)
        cookies_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.cookies_consent))
        )
        # Clicca il pulsante dei cookie
        cookies_button.click()
        # Attendi che il popup dei cookie scompaia dal DOM
        # WebDriverWait(self.driver, 10).until(
        #     EC.invisibility_of_element((By.XPATH, "fc-button-label"))
        # )

    def signup_login(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.login_button))
        ).click()

    #Invece di scrivere 100 volte webdriverwait mi creo un helper
    def wait_and_fill(self, by_type, selector, value):
        """
        Attende che un elemento sia cliccabile e inserisce il valore fornito tramite send_keys.

        :param by_type: Tipo del selettore (esempio: By.ID, By.CSS_SELECTOR).
        :param selector: Identificatore del campo (esempio: "email").
        :param value: Testo da inviare nel campo.
        """
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((by_type, selector))  # Aspetta che il campo sia cliccabile
        )
        element.clear()  # Pulisce il campo (opzionale, se vuoi sovrascrivere il valore precedente)
        element.send_keys(value)  # Inserisce il testo nel campo

    #per attendere e poi cliccare
    def wait_and_click(self, by_type, selector, timeout=10):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((by_type, selector))  # Aspetta che il campo sia cliccabile
        )
        element.click()  # clicca
