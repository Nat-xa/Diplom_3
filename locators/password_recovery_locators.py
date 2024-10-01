from selenium.webdriver.common.by import By


class PasswordRecoveryLocators:

    # Кнопка "Восстановить"
    RECOVERY_BUTTON = [By.XPATH, ".//button[text() = 'Восстановить']"]
    # Поле ввода email в форме восстановления пароля
    EMAIL_INPUT_RECOVERY = [By.XPATH, ".//input[@class = 'text input__textfield text_type_main-default']"]
    # Кнопка "Сохранить" в форме восстановления пароля
    SAVE_BUTTON_RECOVERY_FORM = [By.XPATH, ".//button[@class = 'button_button__33qZ0 button_button_type_primary__"
                                           "1O7Bx button_button_size_medium__3zxIa' and text() = 'Сохранить']"]
    # Кнопка отображения / скрытия пароля
    EYE_BUTTON = [By.XPATH, ".//div[@class = 'input__icon input__icon-action']"]
    # Поле "Пароль" в форме восстановления пароля в активном состоянии
    INPUT_PASSWORD_RECOVERY_ACTIV = [By.XPATH, ".//div[@class = 'input pr-6 pl-6 input_type_text input_size_default "
                                               "input_status_active']"]
