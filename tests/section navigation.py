from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site")

driver.find_element(By.XPATH, "//div/main/section[1]/div[1]/div[2]").click()
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h2[text()='Соусы']")))

driver.find_element(By.XPATH, "//div/main/section[1]/div[1]/div[3]").click()
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h2[text()='Начинки']")))

driver.find_element(By.XPATH, "//div/main/section[1]/div[1]/div[1]").click()
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h2[text()='Булки']")))
