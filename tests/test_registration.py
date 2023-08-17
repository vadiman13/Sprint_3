from selenium.webdriver.common.by import By
from an_additional_task import generate_email
from an_additional_task import generate_password
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import PagesLocators

def test_invalid_password_registration(driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")
    wait = WebDriverWait(driver, 10)
    driver.find_element(By.XPATH, PagesLocators.REGISTRATION_NAME_INPUT).send_keys("Гриша")
    driver.find_element(By.XPATH, PagesLocators.REGISTRATION_EMAIL_INPUT).send_keys(generate_email())
    driver.find_element(By.XPATH, PagesLocators.REGISTRATION_PASSWORD_INPUT).send_keys("12345")
    driver.find_element(By.XPATH, PagesLocators.REGISTRATION_BUTTON).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, PagesLocators.REGISTRATION_ERROR_PASSWORD)))
    assert driver.find_element(By.XPATH, PagesLocators.REGISTRATION_ERROR_PASSWORD).is_displayed(), "Ошибка 'Некорректный пароль' не выведена"

def test_registration(driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")
    wait = WebDriverWait(driver, 10)
    email = generate_email()
    password = generate_password()
    driver.find_element(By.XPATH, PagesLocators.REGISTRATION_NAME_INPUT).send_keys("Гриша")
    driver.find_element(By.XPATH, PagesLocators.REGISTRATION_EMAIL_INPUT).send_keys(email)
    driver.find_element(By.XPATH, PagesLocators.REGISTRATION_PASSWORD_INPUT).send_keys(password)
    driver.find_element(By.XPATH, PagesLocators.REGISTRATION_BUTTON).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, PagesLocators.HOME_BUTTON)))
    driver.find_element(By.XPATH, PagesLocators.HOME_BUTTON).click()
    driver.find_element(By.CSS_SELECTOR, PagesLocators.AUTH_EMAIL_INPUT).send_keys(email)
    driver.find_element(By.CSS_SELECTOR, PagesLocators.AUTH_PASSWORD_INPUT).send_keys(password)
    driver.find_element(By.XPATH, PagesLocators.AUTH_ENTER_BUTTON).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, PagesLocators.HOME_BUTTON)))
    driver.find_element(By.XPATH, PagesLocators.HOME_BUTTON).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, PagesLocators.HOME_LOGIN)))
    email_value = driver.find_element(By.XPATH, PagesLocators.HOME_LOGIN).get_attribute("value")
    assert email_value == email, "Регистрация не пройдена"



