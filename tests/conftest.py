import time

from appium.webdriver import webdriver
import pytest
#chrome driver
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

# L'errore che hai riscontrato potrebbe essere dovuto al fatto che il `pytest` non riconosce l'argomento `--browser_name` perché non gli è stato configurato correttamente.
# Per risolvere questo problema, devi dire a `pytest` di accettare l'opzione `--browser_name` come argomento tramite l'uso di una funzione chiamata `pytest_addoption`.
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="browser selection"
    )


@pytest.fixture(scope="module") #scope="function" si distrugge ad ogni test, se usi module/session no
def browserInstance(request): #request prende ciò che gli metto nella linea di comando (es. firefox o chrome) per capire quale browser avviare
    browser_name = request.config.getoption("browser_name", default="chrome") #quando nel terminale gli metto la linea di comando "pytest test_nomefile.py --browser_name firefox, lui si prende il nome di quest'ultima per capire quale browser usare
    service_obj = Service()
    if browser_name == "chrome":
        driver = webdriver.Chrome(service=service_obj)
        driver.implicitly_wait(4)
    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=service_obj)
        driver.implicitly_wait(4)
    yield driver #qui finisce il setup iniziato in riga 19 con pytest.fixture
    time.sleep(3)
    driver.quit() #teardown