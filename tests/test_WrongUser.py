import random
import string
import time
import pytest
from selenium import webdriver
from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.signup_login_page import SignLogPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Fixture per il browser con scope "module" per condividere tra piu' test così che non ricomincia da capo ogni volta ma riprende da dove ha interrotto altro test
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

#4-8
@pytest.mark.smoke
def test_signup_login(shared_browser_instance):
    # Usa lo stesso browser dalla fixture condivisa
    basepage = BasePage(shared_browser_instance)
    # Usa la homepage già caricata e naviga verso "Signup/Login"
    basepage.signup_login()
    print("Navigato alla pagina di Signup/Login.")

@pytest.mark.smoke
def test_login_fail(shared_browser_instance):
    SigLog = SignLogPage(shared_browser_instance)
    SigLog.signup_button()
    SigLog.fail_login("a@live.it","aaa")



