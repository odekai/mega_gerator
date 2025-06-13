from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_campos_vazios():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://127.0.0.1:5000")

    # Tentando logar sem preencher nada
    driver.find_element(By.CLASS_NAME, "btn-login").click()
    time.sleep(2)

    # Espera uma mensagem de erro ou algo que indique falha
    assert "preencha" in driver.page_source.lower() or "obrigatório" in driver.page_source.lower()
    driver.quit()
