import allure


from pages.main_page import MainPage
from pages.password_recovery_page import PasswordRecoveryPage


class TestPasswordRecoveryPage:

    @allure.title('Проверка перехода на страницу восстановления пароля по кнопку "Восстановить пароль"')
    def test_password_recovery_button(self, driver):
        main_page = MainPage(driver)
        main_page.click_account_button()
        main_page.click_password_recovery_button()
        password_recovery_page = PasswordRecoveryPage(driver)
        element = password_recovery_page.wait_recovery_button()

        assert element.is_enabled

    @allure.title('Проверка работы кнопки "Восстановить" после ввода email')
    def test_recovery_button(self, driver, user_info):
        main_page = MainPage(driver)
        main_page.click_account_button()
        main_page.click_password_recovery_button()
        password_recovery_page = PasswordRecoveryPage(driver)
        password_recovery_page.set_email_input_recovery(user_info[0])
        password_recovery_page.click_recovery_button()
        element = password_recovery_page.wait_save_button()

        assert element.is_enabled

    @allure.title('Проверка активности поля при клике по кнопке "Показать/скрыть пароль"')
    def test_eye_button(self, driver, user_info):
        main_page = MainPage(driver)
        main_page.click_account_button()
        main_page.click_password_recovery_button()
        password_recovery_page = PasswordRecoveryPage(driver)
        password_recovery_page.set_email_input_recovery(user_info[0])
        password_recovery_page.click_recovery_button()
        password_recovery_page.click_eye_button()
        element = password_recovery_page.wait_activ_input_password()

        assert element.is_displayed
