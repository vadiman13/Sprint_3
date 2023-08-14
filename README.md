# Проект автоматизации тестирования сервиса Stellar Burgers.

Основа для написания автотестов — фреймворк Selenium.

## 1. Тестирование регистрации - test_registration
### 1.1 Ошибка для некорректного пароля

```python
driver.get("https://stellarburgers.nomoreparties.site/register")
driver.find_element(By.CSS_SELECTOR, "#root > div > main > div > form > fieldset:nth-child(1) > div > div > input").send_keys("Гриша")
driver.find_element(By.CSS_SELECTOR, "#root > div > main > div > form > fieldset:nth-child(2) > div > div > input").send_keys("example@example.com")
driver.find_element(By.CSS_SELECTOR, "#root > div > main > div > form > fieldset:nth-child(3) > div > div > input").send_keys("32fr2")
driver.find_element(By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]").click()
driver.find_element(By.XPATH, "//*[contains(text(), 'Некорректный пароль')]")
time.sleep(3)
assert driver.current_url == 'https://stellarburgers.nomoreparties.site/register', f"Ожидается URL - https://stellarburgers.nomoreparties.site/register, текущий URL: {driver.current_url}"
```
### Используемые локаторы:
1) Поле ввода имени - CSS_SELECTOR: "#root > div > main > div > form > fieldset:nth-child(1) > div > div > input"
2) Поле ввода email - CSS_SELECTOR: "#root > div > main > div > form > fieldset:nth-child(2) > div > div > input"
3) Поле ввода пароля - CSS_SELECTOR: "#root > div > main > div > form > fieldset:nth-child(3) > div > div > input"
4) Кнопка "Зарегестрироваться" - XPATH: "//button[contains(text(), 'Зарегистрироваться')]"
5) Текст ошибки пароля - XPATH: "//*[contains(text(), 'Некорректный пароль')]"

### 1.2 Успешная регистрация
```python
driver.get("https://stellarburgers.nomoreparties.site/register")
driver.find_element(By.CSS_SELECTOR, "#root > div > main > div > form > fieldset:nth-child(1) > div > div > input").send_keys("Вадим")
driver.find_element(By.CSS_SELECTOR, "#root > div > main > div > form > fieldset:nth-child(2) > div > div > input").send_keys("vadimkotyukov12932@yandex.ru")
driver.find_element(By.CSS_SELECTOR, "#root > div > main > div > form > fieldset:nth-child(3) > div > div > input").send_keys("32fr21")
driver.find_element(By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]").click()
time.sleep(10)
assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login', f"Ожидается URL - https://stellarburgers.nomoreparties.site/login, текущий URL: {driver.current_url}"
```
### Используемые локаторы:
1) Поле ввода имени - CSS_SELECTOR: "#root > div > main > div > form > fieldset:nth-child(1) > div > div > input"
2) Поле ввода email - CSS_SELECTOR: "#root > div > main > div > form > fieldset:nth-child(2) > div > div > input"
3) Поле ввода пароля - CSS_SELECTOR: "#root > div > main > div > form > fieldset:nth-child(3) > div > div > input"
4) Кнопка "Зарегестрироваться" - XPATH: "//button[contains(text(), 'Зарегистрироваться')]"
5) Текст ошибки пароля - XPATH: "//*[contains(text(), 'Некорректный пароль')]"

## 2. Тестирование авторизации - test_enter
### 2.1 вход по кнопке «Войти в аккаунт» на главной
```python
driver.get("https://stellarburgers.nomoreparties.site/")
driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()
driver.find_element(By.CSS_SELECTOR, "input.text[type='text'][name='name']").send_keys("vadimkotyukov12999@yandex.ru")
driver.find_element(By.CSS_SELECTOR, "input.text[type='password'][name='Пароль']").send_keys("32fr21")
driver.find_element(By.XPATH, "//button[text()='Войти']").click()
time.sleep(3)
assert driver.current_url == 'https://stellarburgers.nomoreparties.site/', f"Ожидается URL - https://stellarburgers.nomoreparties.site/, текущий URL: {driver.current_url}"
```
### Используемые локаторы:
1) Кнопка "Войти в аккаунт" - XPATH, "//button[text()='Войти в аккаунт']"
2) Поле ввода логина - CSS_SELECTOR: "input.text[type='text'][name='name']"
3) Поле ввода логина - CSS_SELECTOR: "input.text[type='password'][name='Пароль']"
4) Кнопка "Войти" - XPATH: "//button[text()='Войти']"

### 2.2 вход через кнопку «Личный кабинет»
```python
driver.get("https://stellarburgers.nomoreparties.site/")
driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
driver.find_element(By.CSS_SELECTOR, "input.text[type='text'][name='name']").send_keys("vadimkotyukov12999@yandex.ru")
driver.find_element(By.CSS_SELECTOR, "input.text[type='password'][name='Пароль']").send_keys("32fr21")
driver.find_element(By.XPATH, "//button[text()='Войти']").click()
time.sleep(3)
assert driver.current_url == 'https://stellarburgers.nomoreparties.site/', f"Ожидается URL - https://stellarburgers.nomoreparties.site/, текущий URL: {driver.current_url}"
```
### Используемые локаторы:
1) Кнопка "Личный кабинет" - LINK_TEXT: "Личный Кабинет"
2) Поле ввода логина - CSS_SELECTOR: "input.text[type='text'][name='name']"
3) Поле ввода логина - CSS_SELECTOR: "input.text[type='password'][name='Пароль']"
4) Кнопка "Войти" - XPATH: "//button[text()='Войти']"

### 2.3 вход через кнопку в форме регистрации
```python
driver.get("https://stellarburgers.nomoreparties.site/register")
driver.find_element(By.LINK_TEXT, "Войти").click()
driver.find_element(By.CSS_SELECTOR, "input.text[type='text'][name='name']").send_keys("vadimkotyukov12999@yandex.ru")
driver.find_element(By.CSS_SELECTOR, "input.text[type='password'][name='Пароль']").send_keys("32fr21")
driver.find_element(By.XPATH, "//button[text()='Войти']").click()
time.sleep(3)
assert driver.current_url == 'https://stellarburgers.nomoreparties.site/', f"Ожидается URL - https://stellarburgers.nomoreparties.site/, текущий URL: {driver.current_url}"
```
### Используемые локаторы:
1) Кнопка "Войти" - LINK_TEXT: "Войти"
2) Поле ввода логина - CSS_SELECTOR: "input.text[type='text'][name='name']"
3) Поле ввода логина - CSS_SELECTOR: "input.text[type='password'][name='Пароль']"
4) Кнопка "Войти" - XPATH: "//button[text()='Войти']"

### 2.4 вход через кнопку в форме восстановления пароля
```python
driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
driver.find_element(By.LINK_TEXT, "Войти").click()
driver.find_element(By.CSS_SELECTOR, "input.text[type='text'][name='name']").send_keys("vadimkotyukov12999@yandex.ru")
driver.find_element(By.CSS_SELECTOR, "input.text[type='password'][name='Пароль']").send_keys("32fr21")
driver.find_element(By.XPATH, "//button[text()='Войти']").click()
time.sleep(3)
assert driver.current_url == 'https://stellarburgers.nomoreparties.site/', f"Ожидается URL - https://stellarburgers.nomoreparties.site/, текущий URL: {driver.current_url}"
```
### Используемые локаторы:
1) Кнопка "Войти" - LINK_TEXT: "Войти"
2) Поле ввода логина - CSS_SELECTOR: "input.text[type='text'][name='name']"
3) Поле ввода логина - CSS_SELECTOR: "input.text[type='password'][name='Пароль']"
4) Кнопка "Войти" - XPATH: "//button[text()='Войти']"

## 3. Тестирование перехода в личный кабинет по клику на «Личный кабинет» - test_home
```python
driver.get("https://stellarburgers.nomoreparties.site/login")
driver.find_element(By.CSS_SELECTOR, "input.text[type='text'][name='name']").send_keys("vadimkotyukov12999@yandex.ru")
driver.find_element(By.CSS_SELECTOR, "input.text[type='password'][name='Пароль']").send_keys("32fr21")
driver.find_element(By.XPATH, "//button[text()='Войти']").click()
driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
time.sleep(3)
assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile', f"Ожидается URL - https://stellarburgers.nomoreparties.site/account/profile, текущий URL: {driver.current_url}"
```
### Используемые локаторы:
1) Поле ввода логина - CSS_SELECTOR: "input.text[type='text'][name='name']"
2) Поле ввода логина - CSS_SELECTOR: "input.text[type='password'][name='Пароль']"
3) Кнопка "Войти" - XPATH: "//button[text()='Войти']"
4) Кнопка "Личный кабинет" - LINK_TEXT: "Личный Кабинет"

## 4. Тестистирование перехода в «Конструктор» 
### 4.1 по клику на «Конструктор» 
```python
driver.get("https://stellarburgers.nomoreparties.site/login")
driver.find_element(By.CSS_SELECTOR, "input.text[type='text'][name='name']").send_keys("vadimkotyukov12999@yandex.ru")
driver.find_element(By.CSS_SELECTOR, "input.text[type='password'][name='Пароль']").send_keys("32fr21")
driver.find_element(By.XPATH, "//button[text()='Войти']").click()
driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
driver.find_element(By.XPATH, "//p[text()='Конструктор']").click()
time.sleep(3)
assert driver.current_url == 'https://stellarburgers.nomoreparties.site/', f"Ожидается URL - https://stellarburgers.nomoreparties.site/, текущий URL: {driver.current_url}"
```
### Используемые локаторы:
1) Поле ввода логина - CSS_SELECTOR: "input.text[type='text'][name='name']"
2) Поле ввода логина - CSS_SELECTOR: "input.text[type='password'][name='Пароль']"
3) Кнопка "Войти" - XPATH: "//button[text()='Войти']"
4) Кнопка "Личный кабинет" - LINK_TEXT: "Личный Кабинет"
5) Кнопка "Конструктор" - XPATH: "//p[text()='Конструктор']

### 4.2 по клику на логотип Stellar Burgers
```Python
driver.get("https://stellarburgers.nomoreparties.site/login")
driver.find_element(By.CSS_SELECTOR, "input.text[type='text'][name='name']").send_keys("vadimkotyukov12999@yandex.ru")
driver.find_element(By.CSS_SELECTOR, "input.text[type='password'][name='Пароль']").send_keys("32fr21")
driver.find_element(By.XPATH, "//button[text()='Войти']").click()
driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
driver.find_element(By.XPATH, "//*[contains(@class, 'AppHeader_header__logo')]").click()
time.sleep(3)
assert driver.current_url == 'https://stellarburgers.nomoreparties.site/', f"Ожидается URL - https://stellarburgers.nomoreparties.site/, текущий URL: {driver.current_url}"
```
### Используемые локаторы:
1) Поле ввода логина - CSS_SELECTOR: "input.text[type='text'][name='name']"
2) Поле ввода логина - CSS_SELECTOR: "input.text[type='password'][name='Пароль']"
3) Кнопка "Войти" - XPATH: "//button[text()='Войти']"
4) Кнопка "Личный кабинет" - LINK_TEXT: "Личный Кабинет"
5) Лого - XPATH: "//*[contains(@class, 'AppHeader_header__logo')]"

## 5. Тестирование выхода из аккаунта по кнопке «Выйти» в личном кабинете - test_exit
```python
driver.get("https://stellarburgers.nomoreparties.site/login")
driver.find_element(By.CSS_SELECTOR, "input.text[type='text'][name='name']").send_keys("vadimkotyukov12999@yandex.ru")
driver.find_element(By.CSS_SELECTOR, "input.text[type='password'][name='Пароль']").send_keys("32fr21")
driver.find_element(By.XPATH, "//button[text()='Войти']").click()
driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
driver.implicitly_wait(3)
driver.find_element(By.XPATH, "//li[contains(@class, 'Account_listItem')]//button[text()='Выход']").click()
time.sleep(3)
assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login', f"Ожидается URL - https://stellarburgers.nomoreparties.site/login, текущий URL: {driver.current_url}"
```
### Используемые локаторы:
1) Поле ввода логина - CSS_SELECTOR: "input.text[type='text'][name='name']"
2) Поле ввода логина - CSS_SELECTOR: "input.text[type='password'][name='Пароль']"
3) Кнопка "Войти" - XPATH: "//button[text()='Войти']"
4) Кнопка "Личный кабинет" - LINK_TEXT: "Личный Кабинет"
5) Кнопка "Выйти" - XPATH: "//li[contains(@class, 'Account_listItem')]//button[text()='Выход']"

## 6. Тестирование перехода к разделам - test_construct_sections
### 6.1 «Булки»,

```python
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
```
### Используемые локаторы:
1) Пункт списка "Начинки" - By.XPATH: ".//span[text()='Начинки']"
2) Пункт списка "Булки" - XPATH: ".//span[text()='Булки']"
3) Активный раздел списка - CSS_SELECTOR: "div.tab_tab__1SPyG.tab_tab_type_current__2BEPc.pt-4.pr-10.pb-4.pl-10.noselect"

### 6.2 «Соусы»
```python
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
```
### Используемые локаторы:
1) Кнопка "Соусы" - XPATH: ".//span[text()='Соусы']"
2) Активный раздел списка - CSS_SELECTOR: "div.tab_tab__1SPyG.tab_tab_type_current__2BEPc.pt-4.pr-10.pb-4.pl-10.noselect"
    
### 6.3 «Начинки»
```python
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
```
### Используемые локаторы:
1) Кнопка "Соусы" - XPATH: ".//span[text()='Начинки']"
2) Активный раздел списка - CSS_SELECTOR: "div.tab_tab__1SPyG.tab_tab_type_current__2BEPc.pt-4.pr-10.pb-4.pl-10.noselect"
