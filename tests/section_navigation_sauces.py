from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators import Locators
from helpers.helpers import BASE_URL
class TestNavigation:
    def test_section_navigation_sauces_true(self, driver):
        driver.get(BASE_URL)

        driver.find_element(*Locators.BUTTON_SAUCE).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.HEADER_SAUCES)))

        section_header = driver.find_element(*Locators.HEADER_SAUCES)
        assert section_header.is_displayed()