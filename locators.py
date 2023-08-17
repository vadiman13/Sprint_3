
class PagesLocators:

    CONSTRUCT_TABS = '//span[contains(text(), "Начинки") or contains(text(), "Соусы") or contains(text(), "Булки")]'
    CONSTRUCT_SECTIONS = '//h2[contains(text(), "Начинки") or contains(text(), "Соусы") or contains(text(), "Булки")]'
    CONSTRUCT_ENTER = '//button[contains(text(), "Войти в аккаунт")]'
    CONSTRUCT_BUTTON = '//p[contains(text(), "Конструктор")]'
    LOGO = "//*[contains(@class, 'AppHeader_header__logo')]"
    ORDER_BUTTON = '//button[contains(text(), "Оформить заказ")]'

    HOME_BUTTON = '//p[contains(text(), "Личный Кабинет")]'
    HOME_PROFILE_DESCRIPTION = '//p[contains(text(), "В этом разделе вы можете изменить свои персональные данные")]'
    HOME_EXIT_BUTTON = '//li[contains(@class, "Account_listItem")]//button[text()="Выход"]'
    HOME_LOGIN = '//label[text()="Логин"]/following-sibling::input'

    AUTH_PASSWORD_INPUT = "input.text[type='password'][name='Пароль']"
    AUTH_EMAIL_INPUT = "input.text[type='text'][name='name']"
    AUTH_ENTER_BUTTON = '//button[contains(@class, "button_button_type_primary_")]'
    AUTH_FORGOT_PASSWORD = '//a[@href="/forgot-password"]'
    AUTH_REGISTRATION = '//a[@href="/register"]'
    AUTH_TITLE = '//h2[contains(text(), "Вход")]'

    REGISTRATION_ENTER_LINK = '//p[contains(text(), "Личный Кабинет")]'
    REMEMBER_PASSWORD_LINK = '//a[contains(text(), "Войти")]'
    REGISTRATION_PASSWORD_INPUT = "//input[@type='password']"
    REGISTRATION_NAME_INPUT = '//label[text()="Имя"]/following-sibling::input'
    REGISTRATION_EMAIL_INPUT = '//label[text()="Email"]/following-sibling::input'
    REGISTRATION_ERROR_PASSWORD = '//p[contains(text(), "Некорректный пароль")]'
    REGISTRATION_BUTTON = '//button[contains(text(), "Зарегистрироваться")]'


