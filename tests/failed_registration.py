from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from helpers.helpers import generate_login
from locators.locators import Locators
from config.config import REGISTER_URL

class TestFormRegister:
    def test_registration_form_failed(self, driver, generate_login):
        driver.get(REGISTER_URL)
        login = generate_login(length=8)

        driver.find_element(*Locators.INPUT_NAME).send_keys("Burger_Man_13")
        driver.find_element(*Locators.INPUT_LOGIN).send_keys(login)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys('1a2b3')
        driver.find_element(*Locators.BUTTON_REGISTER).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.LABEL_ERROR)))

        assert driver.find_element(*Locators.LABEL_ERROR).is_displayed()

