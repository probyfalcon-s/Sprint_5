from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def test_registration_form(driver, generate_password, generate_login):
    driver.get("https://stellarburgers.nomoreparties.site/register")
    login = generate_login(length=8)

    driver.find_element(By.XPATH, "//div/main/div/form/fieldset[1]/div/div/input").send_keys("Burger_Man_13")
    driver.find_element(By.XPATH, "//div/main/div/form/fieldset[2]/div/div/input").send_keys(login)
    driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys('1a2b3')
    driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']")))

