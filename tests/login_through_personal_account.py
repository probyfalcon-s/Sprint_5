from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site")

driver.find_element(By.XPATH, "//p[text()='Личный Кабинет']").click()

driver.find_element(By.XPATH, "//input[@name='name']").send_keys("alexeysokolov13987@yandex.ru")
driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys("dBAn]C")
driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa'] ").click()

WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[text()='Оформить заказ']")))
