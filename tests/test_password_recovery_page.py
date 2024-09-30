import allure

from api_shop.api_shop import ApiShop
from helpers.generation_data import GenerationData
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
    def test_recovery_button(self, driver):
        create_response = ApiShop.create_user(GenerationData.create_valid_user_body())
        user_email = create_response.json()['user']['email']
        headers = GenerationData.get_auth_token_and_create_headers(create_response)
        main_page = MainPage(driver)
        main_page.click_account_button()
        main_page.click_password_recovery_button()
        password_recovery_page = PasswordRecoveryPage(driver)
        password_recovery_page.set_email_input_recovery(user_email)
        password_recovery_page.click_recovery_button()
        element = password_recovery_page.wait_save_button()
        ApiShop.delete_user(headers)

        assert element.is_enabled

    @allure.title('Проверка активности поля при клике по кнопке "Показать/скрыть пароль"')
    def test_eye_button(self, driver):
        create_response = ApiShop.create_user(GenerationData.create_valid_user_body())
        user_email = create_response.json()['user']['email']
        headers = GenerationData.get_auth_token_and_create_headers(create_response)
        main_page = MainPage(driver)
        main_page.click_account_button()
        main_page.click_password_recovery_button()
        password_recovery_page = PasswordRecoveryPage(driver)
        password_recovery_page.set_email_input_recovery(user_email)
        password_recovery_page.click_recovery_button()
        password_recovery_page.click_eye_button()
        element = password_recovery_page.wait_activ_input_password()
        ApiShop.delete_user(headers)

        assert element.is_displayed
