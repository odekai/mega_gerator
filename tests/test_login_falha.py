from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_login_falha():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://127.0.0.1:5000")

    driver.find_element(By.NAME, "usuario").send_keys("admin")
    driver.find_element(By.NAME, "senha").send_keys("senhaerrada")
    driver.find_element(By.CLASS_NAME, "btn-login").click()

    time.sleep(2)
    assert "Usuário ou senha incorretos" in driver.page_source
    driver.quit()
