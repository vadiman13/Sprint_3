from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import PagesLocators

class TestHome:

    def test_home(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/login")
        driver.find_element(By.CSS_SELECTOR, PagesLocators.AUTH_EMAIL_INPUT).send_keys("vadimkotyukov12999@yandex.ru")
        driver.find_element(By.CSS_SELECTOR, PagesLocators.AUTH_PASSWORD_INPUT).send_keys("32fr21")
        driver.find_element(By.XPATH, PagesLocators.AUTH_ENTER_BUTTON).click()
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, PagesLocators.HOME_BUTTON)))
        driver.find_element(By.XPATH, PagesLocators.HOME_BUTTON).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, PagesLocators.HOME_PROFILE_DESCRIPTION)))
        assert driver.find_element(By.XPATH,
                                   PagesLocators.HOME_PROFILE_DESCRIPTION).is_displayed(), 'Переход в "Личный кабинет" не осуществлен'




