import time

import allure

from locators.password_recovery_locators import PasswordRecoveryLocators
from pages.base_page import BasePage


class PasswordRecoveryPage(BasePage):

    @allure.step('Заполнение Email для восстановление пароля')
    def set_email_input_recovery(self, email):
        email_input = self.wait_and_find_element(PasswordRecoveryLocators.EMAIL_INPUT_RECOVERY)
        email_input.send_keys(email)

    @allure.step('Нажатие на кнопку "Восстановить"')
    def click_recovery_button(self):
        recovery_button = self.wait_and_find_element(PasswordRecoveryLocators.RECOVERY_BUTTON)
        recovery_button.click()

    @allure.step('Нажатие на "глазик" в форме восстановления пароля')
    def click_eye_button(self):
        eye_button = self.wait_and_find_element(PasswordRecoveryLocators.EYE_BUTTON)
        time.sleep(2)
        eye_button.click()

    @allure.step('Ожидание кнопки "Восстановить"')
    def wait_recovery_button(self):
        element = self.wait_and_find_element(PasswordRecoveryLocators.RECOVERY_BUTTON)
        return element

    @allure.step('Ожидание кнопки "Сохранить"')
    def wait_save_button(self):
        element = self.wait_and_find_element(PasswordRecoveryLocators.SAVE_BUTTON_RECOVERY_FORM)
        return element

    @allure.step('Ожидание подсветки при нажатии на "глазик" в форме восстановления пароля')
    def wait_activ_input_password(self):
        element = self.wait_and_find_element(PasswordRecoveryLocators.INPUT_PASSWORD_RECOVERY_ACTIV)
        return element
