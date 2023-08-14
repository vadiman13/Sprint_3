import time

from selenium.webdriver.common.by import By
from selenium import webdriver



# Переход по клику на «Конструктор»
driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/login")
driver.find_element(By.CSS_SELECTOR, "input.text[type='text'][name='name']").send_keys("vadimkotyukov12999@yandex.ru")
driver.find_element(By.CSS_SELECTOR, "input.text[type='password'][name='Пароль']").send_keys("32fr21")
driver.find_element(By.XPATH, "//button[text()='Войти']").click()
driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
driver.find_element(By.XPATH, "//p[text()='Конструктор']").click()
time.sleep(3)
assert driver.current_url == 'https://stellarburgers.nomoreparties.site/', f"Ожидается URL - https://stellarburgers.nomoreparties.site/, текущий URL: {driver.current_url}"
driver.quit()


# Переход по клику на логотип Stellar Burgers.
driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/login")
driver.find_element(By.CSS_SELECTOR, "input.text[type='text'][name='name']").send_keys("vadimkotyukov12999@yandex.ru")
driver.find_element(By.CSS_SELECTOR, "input.text[type='password'][name='Пароль']").send_keys("32fr21")
driver.find_element(By.XPATH, "//button[text()='Войти']").click()
driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
driver.find_element(By.XPATH, "//*[contains(@class, 'AppHeader_header__logo')]").click()
time.sleep(3)
assert driver.current_url == 'https://stellarburgers.nomoreparties.site/', f"Ожидается URL - https://stellarburgers.nomoreparties.site/, текущий URL: {driver.current_url}"
driver.quit()