from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators import Locators
from src.data import TEST_DATA
from config.config import RESTORE_URL

class TestFormLogin:
    def test_login_form_restore_password_true(self, driver):
        driver.get(RESTORE_URL)

        driver.find_element(*Locators.BUTTON_LOGIN_RESTORE).click()

        driver.find_element(*Locators.INPUT_EMAIL_LOGIN).send_keys(TEST_DATA['login'])
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(TEST_DATA['password'])
        driver.find_element(*Locators.BUTTON_LOGIN).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.BUTTON_ORDER)))

        assert driver.find_element(*Locators.BUTTON_ORDER).is_displayed()
