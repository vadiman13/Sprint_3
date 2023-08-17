from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import PagesLocators

def test_menu_tabs(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    tabs = driver.find_elements(By.XPATH, PagesLocators.CONSTRUCT_TABS)
    sections = driver.find_elements(By.XPATH, PagesLocators.CONSTRUCT_SECTIONS)
    order = ["Начинки", "Соусы", "Булки"]
    for section_name in order:
        tab_index = [i for i in range(len(tabs)) if tabs[i].text.strip() == section_name][0]
        section_index = [i for i in range(len(sections)) if sections[i].text.strip() == section_name][0]
        tab = tabs[tab_index]
        section = sections[section_index]
        driver.execute_script("arguments[0].click();", tab)
        WebDriverWait(driver, 10).until(EC.visibility_of(section))
        assert section.is_displayed(), "Выбранный раздел не отображен в меню"

def test_menu_scroll(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    tabs = driver.find_elements(By.XPATH, PagesLocators.CONSTRUCT_TABS)
    sections = driver.find_elements(By.XPATH, PagesLocators.CONSTRUCT_SECTIONS)
    for i in range(len(sections) - 1, -1, -1):
        section = sections[i]
        tab = tabs[i]
        driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth' })", section)
        WebDriverWait(driver, 10).until(EC.visibility_of(tab))
        WebDriverWait(driver, 10).until(EC.visibility_of(section))
        assert tab.text.strip() == section.text.strip(), "Неактивен таб текщего раздела меню"
