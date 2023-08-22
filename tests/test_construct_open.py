from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import PagesLocators

class TestConstructOpen:

    def test_construct_button(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/login")
        wait = WebDriverWait(driver, 5)
        driver.find_element(By.CSS_SELECTOR, PagesLocators.AUTH_EMAIL_INPUT).send_keys("vadimkotyukov12999@yandex.ru")
        driver.find_element(By.CSS_SELECTOR, PagesLocators.AUTH_PASSWORD_INPUT).send_keys("32fr21")
        driver.find_element(By.XPATH, PagesLocators.AUTH_ENTER_BUTTON).click()
        driver.find_element(By.XPATH, PagesLocators.HOME_BUTTON).click()
        driver.find_element(By.XPATH, PagesLocators.CONSTRUCT_BUTTON).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, PagesLocators.ORDER_BUTTON)))
        assert driver.find_element(By.XPATH,
                                   PagesLocators.ORDER_BUTTON).is_displayed(), "Переход в Конструктор не осуществлен"

    def test_construct_logo(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/login")
        wait = WebDriverWait(driver, 5)
        driver.find_element(By.CSS_SELECTOR, PagesLocators.AUTH_EMAIL_INPUT).send_keys("vadimkotyukov12999@yandex.ru")
        driver.find_element(By.CSS_SELECTOR, PagesLocators.AUTH_PASSWORD_INPUT).send_keys("32fr21")
        driver.find_element(By.XPATH, PagesLocators.AUTH_ENTER_BUTTON).click()
        driver.find_element(By.XPATH, PagesLocators.HOME_BUTTON).click()
        driver.find_element(By.XPATH, PagesLocators.LOGO).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, PagesLocators.ORDER_BUTTON)))
        assert driver.find_element(By.XPATH,
                                   PagesLocators.ORDER_BUTTON).is_displayed(), "Переход в Конструктор не осуществлен"


