from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import PagesLocators

class TestExit:

    def test_exit(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/login")
        wait = WebDriverWait(driver, 5)
        driver.find_element(By.CSS_SELECTOR, PagesLocators.AUTH_EMAIL_INPUT).send_keys("vadimkotyukov12999@yandex.ru")
        driver.find_element(By.CSS_SELECTOR, PagesLocators.AUTH_PASSWORD_INPUT).send_keys("32fr21")
        driver.find_element(By.XPATH, PagesLocators.AUTH_ENTER_BUTTON).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, PagesLocators.HOME_BUTTON)))
        driver.find_element(By.XPATH, PagesLocators.HOME_BUTTON).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, PagesLocators.HOME_EXIT_BUTTON)))
        driver.find_element(By.XPATH, PagesLocators.HOME_EXIT_BUTTON).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, PagesLocators.AUTH_TITLE)))
        assert driver.find_element(By.XPATH,
                                   PagesLocators.AUTH_TITLE).is_displayed(), "Выход из учетной записи не произошел"


