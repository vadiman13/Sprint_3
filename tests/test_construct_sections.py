from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import PagesLocators


def test_tab_fillings(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    wait = WebDriverWait(driver, 5)
    driver.find_element(By.XPATH, PagesLocators.CONSTRUCT_TAB_FILLINGS).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, PagesLocators.CONSTRUCT_SECTION_FILLINGS)))
    assert driver.find_element(By.XPATH, PagesLocators.CONSTRUCT_SECTION_FILLINGS).is_displayed(), "Выбранный раздел не отображен в меню"

def test_tab_souces(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    wait = WebDriverWait(driver, 5)
    driver.find_element(By.XPATH, PagesLocators.CONSTRUCT_TAB_FILLINGS).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, PagesLocators.CONSTRUCT_SECTION_FILLINGS)))
    tab_sources = driver.find_element(By.XPATH, PagesLocators.CONSTRUCT_TAB_SOUCES)
    driver.execute_script("arguments[0].click();", tab_sources)
    wait.until(EC.visibility_of_element_located((By.XPATH, PagesLocators.CONSTRUCT_SECTION_SOUCES)))
    assert driver.find_element(By.XPATH, PagesLocators.CONSTRUCT_SECTION_SOUCES).is_displayed(), "Выбранный раздел не отображен в меню"

def test_tab_buns(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    wait = WebDriverWait(driver, 10)
    driver.find_element(By.XPATH, PagesLocators.CONSTRUCT_TAB_FILLINGS).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, PagesLocators.CONSTRUCT_SECTION_FILLINGS)))
    tab_buns = driver.find_element(By.XPATH, PagesLocators.CONSTRUCT_TAB_BUNS)
    driver.execute_script("arguments[0].click();", tab_buns)
    wait.until(EC.visibility_of_element_located((By.XPATH, PagesLocators.CONSTRUCT_SECTION_BUNS)))
    assert driver.find_element(By.XPATH, PagesLocators.CONSTRUCT_SECTION_BUNS).is_displayed(), "Выбранный раздел не отображен в меню"

