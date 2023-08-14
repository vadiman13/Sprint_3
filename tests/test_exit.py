import time
from selenium.webdriver.common.by import By
from selenium import webdriver


# Выход по кнопке «Выйти» в личном кабинете.
driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/login")
driver.find_element(By.CSS_SELECTOR, "input.text[type='text'][name='name']").send_keys("vadimkotyukov12999@yandex.ru")
driver.find_element(By.CSS_SELECTOR, "input.text[type='password'][name='Пароль']").send_keys("32fr21")
driver.find_element(By.XPATH, "//button[text()='Войти']").click()
driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
driver.implicitly_wait(3)
driver.find_element(By.XPATH, "//li[contains(@class, 'Account_listItem')]//button[text()='Выход']").click()
time.sleep(3)
assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login', f"Ожидается URL - https://stellarburgers.nomoreparties.site/login, текущий URL: {driver.current_url}"
driver.quit()
