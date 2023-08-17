# Проект автоматизации тестирования сервиса Stellar Burgers.

Основа для написания автотестов — фреймворк Selenium.

## 1. Тестирование регистрации - test_registration
### 1.1 Ошибка для некорректного пароля
```python
driver.get("https://stellarburgers.nomoreparties.site/register")
    wait = WebDriverWait(driver, 10)
    driver.find_element(By.XPATH, PagesLocators.REGISTRATION_NAME_INPUT).send_keys("Гриша")
    driver.find_element(By.XPATH, PagesLocators.REGISTRATION_EMAIL_INPUT).send_keys(generate_email())
    driver.find_element(By.XPATH, PagesLocators.REGISTRATION_PASSWORD_INPUT).send_keys("12345")
    driver.find_element(By.XPATH, PagesLocators.REGISTRATION_BUTTON).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, PagesLocators.REGISTRATION_ERROR_PASSWORD)))
    assert driver.find_element(By.XPATH, PagesLocators.REGISTRATION_ERROR_PASSWORD).is_displayed(), "Ошибка 'Некорректный пароль' не выведена"
```
### 1.2 Успешная регистрация
```python
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
```

## 2. Тестирование авторизации - test_enter
### 2.1 вход по кнопке «Войти в аккаунт» на главной
```python
def test_enter_home_button(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    wait = WebDriverWait(driver, 5)
    driver.find_element(By.XPATH, PagesLocators.HOME_BUTTON).click()
    driver.find_element(By.CSS_SELECTOR, PagesLocators.AUTH_EMAIL_INPUT).send_keys("vadimkotyukov12999@yandex.ru")
    driver.find_element(By.CSS_SELECTOR, PagesLocators.AUTH_PASSWORD_INPUT).send_keys("32fr21")
    driver.find_element(By.XPATH, PagesLocators.AUTH_ENTER_BUTTON).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, PagesLocators.ORDER_BUTTON)))
    assert driver.find_element(By.XPATH, PagesLocators.ORDER_BUTTON).is_displayed(), "Авторизация не пройдена"
```
### 2.2 вход через кнопку «Личный кабинет»
```python
def test_enter_registration_button(driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")
    wait = WebDriverWait(driver, 5)
    driver.find_element(By.XPATH, PagesLocators.REGISTRATION_ENTER_LINK).click()
    driver.find_element(By.CSS_SELECTOR, PagesLocators.AUTH_EMAIL_INPUT).send_keys("vadimkotyukov12999@yandex.ru")
    driver.find_element(By.CSS_SELECTOR, PagesLocators.AUTH_PASSWORD_INPUT).send_keys("32fr21")
    driver.find_element(By.XPATH, PagesLocators.AUTH_ENTER_BUTTON).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, PagesLocators.ORDER_BUTTON)))
    assert driver.find_element(By.XPATH, PagesLocators.ORDER_BUTTON).is_displayed(), "Авторизация не пройдена"
```
### 2.3 вход через кнопку в форме регистрации
```python
def test_enter_forgot_button(driver):
    driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
    wait = WebDriverWait(driver, 5)
    driver.find_element(By.XPATH, PagesLocators.REMEMBER_PASSWORD_LINK).click()
    driver.find_element(By.CSS_SELECTOR, PagesLocators.AUTH_EMAIL_INPUT).send_keys("vadimkotyukov12999@yandex.ru")
    driver.find_element(By.CSS_SELECTOR, PagesLocators.AUTH_PASSWORD_INPUT).send_keys("32fr21")
    driver.find_element(By.XPATH, PagesLocators.AUTH_ENTER_BUTTON).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, PagesLocators.ORDER_BUTTON)))
    assert driver.find_element(By.XPATH, PagesLocators.ORDER_BUTTON).is_displayed(), "Авторизация не пройдена"
```
### 2.4 вход через кнопку в форме восстановления пароля
```python
def test_enter_head_button(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    wait = WebDriverWait(driver, 5)
    driver.find_element(By.XPATH, PagesLocators.CONSTRUCT_ENTER).click()
    driver.find_element(By.CSS_SELECTOR, PagesLocators.AUTH_EMAIL_INPUT).send_keys("vadimkotyukov12999@yandex.ru")
    driver.find_element(By.CSS_SELECTOR, PagesLocators.AUTH_PASSWORD_INPUT).send_keys("32fr21")
    driver.find_element(By.XPATH, PagesLocators.AUTH_ENTER_BUTTON).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, PagesLocators.ORDER_BUTTON)))
    assert driver.find_element(By.XPATH, PagesLocators.ORDER_BUTTON).is_displayed(), "Авторизация не пройдена"
```

## 3. Тестирование перехода в личный кабинет по клику на «Личный кабинет» - test_home
```python
def test_home(driver):
    driver.get("https://stellarburgers.nomoreparties.site/login")
    driver.find_element(By.CSS_SELECTOR, PagesLocators.AUTH_EMAIL_INPUT).send_keys("vadimkotyukov12999@yandex.ru")
    driver.find_element(By.CSS_SELECTOR, PagesLocators.AUTH_PASSWORD_INPUT).send_keys("32fr21")
    driver.find_element(By.XPATH, PagesLocators.AUTH_ENTER_BUTTON).click()
    wait = WebDriverWait(driver, 5)
    wait.until(EC.visibility_of_element_located((By.XPATH, PagesLocators.HOME_BUTTON)))
    driver.find_element(By.XPATH, PagesLocators.HOME_BUTTON).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, PagesLocators.HOME_PROFILE_DESCRIPTION)))
    assert driver.find_element(By.XPATH, PagesLocators.HOME_PROFILE_DESCRIPTION).is_displayed(), 'Переход в "Личный кабинет" не осуществлен'
```

## 4. Тестистирование перехода в «Конструктор» 
### 4.1 по клику на «Конструктор» 
```python
def test_construct_button(driver):
    driver.get("https://stellarburgers.nomoreparties.site/login")
    wait = WebDriverWait(driver, 5)
    driver.find_element(By.CSS_SELECTOR, PagesLocators.AUTH_EMAIL_INPUT).send_keys("vadimkotyukov12999@yandex.ru")
    driver.find_element(By.CSS_SELECTOR, PagesLocators.AUTH_PASSWORD_INPUT).send_keys("32fr21")
    driver.find_element(By.XPATH, PagesLocators.AUTH_ENTER_BUTTON).click()
    driver.find_element(By.XPATH, PagesLocators.HOME_BUTTON).click()
    driver.find_element(By.XPATH, PagesLocators.CONSTRUCT_BUTTON).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, PagesLocators.ORDER_BUTTON)))
    assert driver.find_element(By.XPATH, PagesLocators.ORDER_BUTTON).is_displayed(), "Переход в Конструктор не осуществлен"
```
### 4.2 по клику на логотип Stellar Burgers
```Python
def test_construct_logo(driver):
    driver.get("https://stellarburgers.nomoreparties.site/login")
    wait = WebDriverWait(driver, 5)
    driver.find_element(By.CSS_SELECTOR, PagesLocators.AUTH_EMAIL_INPUT).send_keys("vadimkotyukov12999@yandex.ru")
    driver.find_element(By.CSS_SELECTOR, PagesLocators.AUTH_PASSWORD_INPUT).send_keys("32fr21")
    driver.find_element(By.XPATH, PagesLocators.AUTH_ENTER_BUTTON).click()
    driver.find_element(By.XPATH, PagesLocators.HOME_BUTTON).click()
    driver.find_element(By.XPATH, PagesLocators.LOGO).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, PagesLocators.ORDER_BUTTON)))
    assert driver.find_element(By.XPATH, PagesLocators.ORDER_BUTTON).is_displayed(), "Переход в Конструктор не осуществлен"
```

## 5. Тестирование выхода из аккаунта по кнопке «Выйти» в личном кабинете - test_exit
```python
def test_exit(driver):
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
    assert driver.find_element(By.XPATH, PagesLocators.AUTH_TITLE).is_displayed(), "Выход из учетной записи не произошел"
```

## 6. Тестирование перехода к разделам - test_construct_sections
### 6.1 Проверка скролла меню при клике на таб
```python
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
```
### 6.2 Тестирование активации таба при скролле меню
```python
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
```