from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_sucesso():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://127.0.0.1:5000")

    driver.find_element(By.NAME, "usuario").send_keys("admin")
    driver.find_element(By.NAME, "senha").send_keys("1234")
    driver.find_element(By.CLASS_NAME, "btn-login").click()

    WebDriverWait(driver,2).until(
        EC.title_contains("Gerenciador") # Espera carregar
    )  

    # Verifica se tá na página principal (ajusta se o título for outro)
    assert "Gerenciador" in driver.page_source

    driver.save_screenshot("tests/evidencias/login_sucesso.png")
    driver.quit()
