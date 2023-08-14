import time

from selenium.webdriver.common.by import By
from selenium import webdriver


# Вход через кнопку "Личный кабинет"
driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")
driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
driver.find_element(By.CSS_SELECTOR, "input.text[type='text'][name='name']").send_keys("vadimkotyukov12999@yandex.ru")
driver.find_element(By.CSS_SELECTOR, "input.text[type='password'][name='Пароль']").send_keys("32fr21")
driver.find_element(By.XPATH, "//button[text()='Войти']").click()
time.sleep(3)
assert driver.current_url == 'https://stellarburgers.nomoreparties.site/', f"Ожидается URL - https://stellarburgers.nomoreparties.site/, текущий URL: {driver.current_url}"
driver.quit()


# Вход через кнопку в форме регистрации
driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/register")
driver.find_element(By.LINK_TEXT, "Войти").click()
driver.find_element(By.CSS_SELECTOR, "input.text[type='text'][name='name']").send_keys("vadimkotyukov12999@yandex.ru")
driver.find_element(By.CSS_SELECTOR, "input.text[type='password'][name='Пароль']").send_keys("32fr21")
driver.find_element(By.XPATH, "//button[text()='Войти']").click()
time.sleep(3)
assert driver.current_url == 'https://stellarburgers.nomoreparties.site/', f"Ожидается URL - https://stellarburgers.nomoreparties.site/, текущий URL: {driver.current_url}"
driver.quit()


# Вход через кнопку в форме восстановления пароля.
driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
driver.find_element(By.LINK_TEXT, "Войти").click()
driver.find_element(By.CSS_SELECTOR, "input.text[type='text'][name='name']").send_keys("vadimkotyukov12999@yandex.ru")
driver.find_element(By.CSS_SELECTOR, "input.text[type='password'][name='Пароль']").send_keys("32fr21")
driver.find_element(By.XPATH, "//button[text()='Войти']").click()
time.sleep(3)
assert driver.current_url == 'https://stellarburgers.nomoreparties.site/', f"Ожидается URL - https://stellarburgers.nomoreparties.site/, текущий URL: {driver.current_url}"
driver.quit()


# Вход по кнопке «Войти в аккаунт» на главной,
driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")
driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()
driver.find_element(By.CSS_SELECTOR, "input.text[type='text'][name='name']").send_keys("vadimkotyukov12999@yandex.ru")
driver.find_element(By.CSS_SELECTOR, "input.text[type='password'][name='Пароль']").send_keys("32fr21")
driver.find_element(By.XPATH, "//button[text()='Войти']").click()
time.sleep(3)
assert driver.current_url == 'https://stellarburgers.nomoreparties.site/', f"Ожидается URL - https://stellarburgers.nomoreparties.site/, текущий URL: {driver.current_url}"
driver.quit()