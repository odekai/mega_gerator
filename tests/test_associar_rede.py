from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_associar_rede():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://127.0.0.1:5000")

    driver.find_element(By.NAME, "usuario").send_keys("admin")
    driver.find_element(By.NAME, "senha").send_keys("1234")
    driver.find_element(By.CLASS_NAME, "btn-login").click()

    time.sleep(1)

    # Gera uma senha
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(1)

    # Preenche rede social e envia
    driver.find_element(By.NAME, "rede").send_keys("Instagram")
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(2)

    assert "Instagram" in driver.page_source
    driver.quit()
