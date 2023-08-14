import time
from selenium.webdriver.common.by import By
from selenium import webdriver


# Ошибка для некорректного пароля
driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/register")
driver.find_element(By.CSS_SELECTOR, "#root > div > main > div > form > fieldset:nth-child(1) > div > div > input").send_keys("Гриша")
driver.find_element(By.CSS_SELECTOR, "#root > div > main > div > form > fieldset:nth-child(2) > div > div > input").send_keys("example@example.com")
driver.find_element(By.CSS_SELECTOR, "#root > div > main > div > form > fieldset:nth-child(3) > div > div > input").send_keys("32fr2")
driver.find_element(By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]").click()
driver.find_element(By.XPATH, "//*[contains(text(), 'Некорректный пароль')]")
time.sleep(3)
assert driver.current_url == 'https://stellarburgers.nomoreparties.site/register', f"Ожидается URL - https://stellarburgers.nomoreparties.site/register, текущий URL: {driver.current_url}"
driver.quit()



# Успешная регистрация
driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/register")
driver.find_element(By.CSS_SELECTOR, "#root > div > main > div > form > fieldset:nth-child(1) > div > div > input").send_keys("Вадим")
driver.find_element(By.CSS_SELECTOR, "#root > div > main > div > form > fieldset:nth-child(2) > div > div > input").send_keys("vadimkotyukov12932@yandex.ru")
driver.find_element(By.CSS_SELECTOR, "#root > div > main > div > form > fieldset:nth-child(3) > div > div > input").send_keys("32fr21")
driver.find_element(By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]").click()
time.sleep(10)
assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login', f"Ожидается URL - https://stellarburgers.nomoreparties.site/login, текущий URL: {driver.current_url}"
driver.quit()

