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
### 6.1 Проверка перехода в раздел "Начинки"
```python
def test_tab_fillings(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    wait = WebDriverWait(driver, 5)
    driver.find_element(By.XPATH, PagesLocators.CONSTRUCT_TAB_FILLINGS).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, PagesLocators.CONSTRUCT_SECTION_FILLINGS)))
    assert driver.find_element(By.XPATH, PagesLocators.CONSTRUCT_SECTION_FILLINGS).is_displayed(), "Выбранный раздел не отображен в меню"
```
### 6.2 Проверка перехода в раздел "Соусы"
```python
def test_tab_souces(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    wait = WebDriverWait(driver, 5)
    driver.find_element(By.XPATH, PagesLocators.CONSTRUCT_TAB_FILLINGS).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, PagesLocators.CONSTRUCT_SECTION_FILLINGS)))
    tab_sources = driver.find_element(By.XPATH, PagesLocators.CONSTRUCT_TAB_SOUCES)
    driver.execute_script("arguments[0].click();", tab_sources)
    wait.until(EC.visibility_of_element_located((By.XPATH, PagesLocators.CONSTRUCT_SECTION_SOUCES)))
    assert driver.find_element(By.XPATH, PagesLocators.CONSTRUCT_SECTION_SOUCES).is_displayed(), "Выбранный раздел не отображен в меню"
```
### 6.3 Проверка перехода в раздел "Булки"
```python
def test_tab_buns(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    wait = WebDriverWait(driver, 10)
    driver.find_element(By.XPATH, PagesLocators.CONSTRUCT_TAB_FILLINGS).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, PagesLocators.CONSTRUCT_SECTION_FILLINGS)))
    tab_buns = driver.find_element(By.XPATH, PagesLocators.CONSTRUCT_TAB_BUNS)
    driver.execute_script("arguments[0].click();", tab_buns)
    wait.until(EC.visibility_of_element_located((By.XPATH, PagesLocators.CONSTRUCT_SECTION_BUNS)))
    assert driver.find_element(By.XPATH, PagesLocators.CONSTRUCT_SECTION_BUNS).is_displayed(), "Выбранный раздел не отображен в меню"
```