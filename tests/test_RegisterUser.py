import time
import pytest
from selenium import webdriver
from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.signup_login_page import SignLogPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Fixture per il browser con scope "module" per condividere tra piu' test
@pytest.fixture(scope="module")
def shared_browser_instance(browserInstance):
    # Mantieni il browser aperto tra più test
    yield browserInstance
    browserInstance.quit()  # Chiudi il browser solo alla fine del modulo

#1-3
@pytest.mark.smoke
def test_open_homepage(shared_browser_instance):
    homepage = HomePage(shared_browser_instance)
    # 1. Apri Google e naviga
    homepage.load_homepage()

    # 2. Accetta i cookies
    basepage = BasePage(shared_browser_instance)
    basepage.accept_cookies()

    # 3. Verifica che la pagina sia caricata correttamente
    homepage.homepage_visibility()

    if homepage.logo_visibility:
        assert True
        print("Logo is visible")
    else:
        assert False
    print("Homepage caricata correttamente.")
    # Lascio il browser navigato pronto per gli altri test

#4-6
@pytest.mark.smoke
def test_signup_login(shared_browser_instance):
    # Usa lo stesso browser dalla fixture condivisa
    basepage = BasePage(shared_browser_instance)
    # Usa la homepage già caricata e naviga verso "Signup/Login"
    basepage.signup_login()
    print("Navigato alla pagina di Signup/Login.")
    #Verifica che signup è visibile
    SigLog = SignLogPage(shared_browser_instance)
    SigLog.newUserSignup_visibility()
    if SigLog.usersignup_visibility:
        assert True
        print("Signup/Login is visible")
    else:
        assert False
    print("Signup/Login caricata correttamente.")
    SigLog.enterName_email("Kevin", "kevin@live.it")
    SigLog.signup_button()
    print("Signup/Login completato.")
    #Verifica visibilità
    if SigLog.accountinfo_visibility():
        assert True
        print("Enter account infrmation visibile")
    else:
        assert False



