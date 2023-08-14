import time
from selenium import webdriver
from selenium.webdriver.common.by import By



driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")
time.sleep(3)
driver.find_element(By.XPATH, ".//span[text()='Начинки']").click()
time.sleep(3)
try:
    element = driver.find_element(By.CSS_SELECTOR, "div.tab_tab__1SPyG.tab_tab_type_current__2BEPc.pt-4.pr-10.pb-4.pl-10.noselect")
    span_element = element.find_element(By.TAG_NAME, "span")
    text = span_element.text
    assert text == "Начинки", "Выбран неверный раздел"
    print("Выбран раздел начинок")
except:
    print("Выбранный раздел не найден")
time.sleep(3)
driver.quit()



driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")
time.sleep(3)
driver.find_element(By.XPATH, ".//span[text()='Соусы']").click()
time.sleep(3)
try:
    element = driver.find_element(By.CSS_SELECTOR, "div.tab_tab__1SPyG.tab_tab_type_current__2BEPc.pt-4.pr-10.pb-4.pl-10.noselect")
    span_element = element.find_element(By.TAG_NAME, "span")
    text = span_element.text
    assert text == "Соусы", "Выбран неверный раздел"
    print("Выбран раздел соусов")
except:
    print("Выбранный раздел не найден")
time.sleep(3)
driver.quit()



driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")
time.sleep(3)
lower = driver.find_element(By.XPATH, ".//span[text()='Начинки']")
driver.execute_script("arguments[0].scrollIntoView();", lower)
time.sleep(3)
upper = driver.find_element(By.XPATH, ".//span[text()='Булки']")
driver.execute_script("arguments[0].scrollIntoView();", upper)
time.sleep(3)
try:
    element = driver.find_element(By.CSS_SELECTOR, "div.tab_tab__1SPyG.tab_tab_type_current__2BEPc.pt-4.pr-10.pb-4.pl-10.noselect")
    span_element = element.find_element(By.TAG_NAME, "span")
    text = span_element.text
    assert text == "Булки", "Выбран неверный раздел"
    print("Выбран раздел булок")
except:
    print("Выбранный раздел не найден")
time.sleep(3)
driver.quit()