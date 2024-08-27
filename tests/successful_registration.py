from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from helpers.helpers import generate_login, generate_password
from config.config import Locators
from helpers.helpers import REGISTER_URL

class TestFormRegister:
    def test_registration_form_successful(self, driver, generate_login, generate_password):
        driver.get(REGISTER_URL)
        password = generate_password(length=8)
        login = generate_login(length=8)

        driver.find_element(*Locators.INPUT_NAME).send_keys("Burger_Man_13")
        driver.find_element(*Locators.INPUT_LOGIN).send_keys(login)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(password)
        driver.find_element(*Locators.BUTTON_REGISTER).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.LABEL_ENTER)))

        assert driver.find_element(*Locators.LABEL_ENTER).is_displayed()
