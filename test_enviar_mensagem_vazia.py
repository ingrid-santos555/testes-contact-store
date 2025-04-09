import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException, UnexpectedAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_enviar_mensagem_vazia(driver):
    driver.get("https://www.demoblaze.com/")
    driver.find_element(By.LINK_TEXT, "Contact").click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "exampleModalLabel"))
    )
    assert driver.find_element(By.ID, "exampleModalLabel").text == "New message"

    assert driver.find_element(By.ID, "recipient-email")
    assert driver.find_element(By.ID, "recipient-name")
    assert driver.find_element(By.ID, "message-text")

    driver.find_element(By.CSS_SELECTOR, "#exampleModal .btn-primary").click()

    try:
        time.sleep(1)
        alert = driver.switch_to.alert
        print("Alerta detectado (vazio):", alert.text)
        alert.dismiss()
    except (NoAlertPresentException, UnexpectedAlertPresentException):
        pass