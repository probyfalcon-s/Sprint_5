import random

import pytest
import string
from selenium import webdriver

@pytest.fixture
def generate_password():
    def generate_passwords(length=8):
        if length < 6:
            raise ValueError("Минимальный пароль — шесть символов.")
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(length))

    return generate_passwords

@pytest.fixture
def generate_login():
    def generate_logins(length=8):
        if length < 3:
            raise ValueError("Длина логина должна быть не менее 3 символов.")
        characters = string.ascii_letters + string.digits
        login = ''.join(random.choice(characters) for _ in range(length))
        return f'{login}@ya.ru'

    return generate_logins


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


