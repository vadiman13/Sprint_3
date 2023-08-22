from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import PagesLocators

class TestEnter:

    def test_enter_home_button(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        wait = WebDriverWait(driver, 5)
        driver.find_element(By.XPATH, PagesLocators.HOME_BUTTON).click()
        driver.find_element(By.CSS_SELECTOR, PagesLocators.AUTH_EMAIL_INPUT).send_keys("vadimkotyukov12999@yandex.ru")
        driver.find_element(By.CSS_SELECTOR, PagesLocators.AUTH_PASSWORD_INPUT).send_keys("32fr21")
        driver.find_element(By.XPATH, PagesLocators.AUTH_ENTER_BUTTON).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, PagesLocators.ORDER_BUTTON)))
        assert driver.find_element(By.XPATH, PagesLocators.ORDER_BUTTON).is_displayed(), "Авторизация не пройдена"

    def test_enter_registration_button(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        wait = WebDriverWait(driver, 5)
        driver.find_element(By.XPATH, PagesLocators.REGISTRATION_ENTER_LINK).click()
        driver.find_element(By.CSS_SELECTOR, PagesLocators.AUTH_EMAIL_INPUT).send_keys("vadimkotyukov12999@yandex.ru")
        driver.find_element(By.CSS_SELECTOR, PagesLocators.AUTH_PASSWORD_INPUT).send_keys("32fr21")
        driver.find_element(By.XPATH, PagesLocators.AUTH_ENTER_BUTTON).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, PagesLocators.ORDER_BUTTON)))
        assert driver.find_element(By.XPATH, PagesLocators.ORDER_BUTTON).is_displayed(), "Авторизация не пройдена"

    def test_enter_forgot_button(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
        wait = WebDriverWait(driver, 5)
        driver.find_element(By.XPATH, PagesLocators.REMEMBER_PASSWORD_LINK).click()
        driver.find_element(By.CSS_SELECTOR, PagesLocators.AUTH_EMAIL_INPUT).send_keys("vadimkotyukov12999@yandex.ru")
        driver.find_element(By.CSS_SELECTOR, PagesLocators.AUTH_PASSWORD_INPUT).send_keys("32fr21")
        driver.find_element(By.XPATH, PagesLocators.AUTH_ENTER_BUTTON).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, PagesLocators.ORDER_BUTTON)))
        assert driver.find_element(By.XPATH, PagesLocators.ORDER_BUTTON).is_displayed(), "Авторизация не пройдена"

    def test_enter_head_button(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        wait = WebDriverWait(driver, 5)
        driver.find_element(By.XPATH, PagesLocators.CONSTRUCT_ENTER).click()
        driver.find_element(By.CSS_SELECTOR, PagesLocators.AUTH_EMAIL_INPUT).send_keys("vadimkotyukov12999@yandex.ru")
        driver.find_element(By.CSS_SELECTOR, PagesLocators.AUTH_PASSWORD_INPUT).send_keys("32fr21")
        driver.find_element(By.XPATH, PagesLocators.AUTH_ENTER_BUTTON).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, PagesLocators.ORDER_BUTTON)))
        assert driver.find_element(By.XPATH, PagesLocators.ORDER_BUTTON).is_displayed(), "Авторизация не пройдена"
