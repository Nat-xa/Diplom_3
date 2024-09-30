import allure

from api_shop.api_shop import ApiShop
from helpers.generation_data import GenerationData
from pages.lk_page import LkPage
from pages.main_page import MainPage
from urls import Urls


class TestLkPage:

    @allure.title('Проверка перехода по клику на "Личный Кабинет"')
    def test_lk_button(self, driver):
        body = GenerationData.create_valid_user_body()
        create_response = ApiShop.create_user(body)
        user_email = create_response.json()['user']['email']
        user_password = body['password']
        headers = GenerationData.get_auth_token_and_create_headers(create_response)
        main_page = MainPage(driver)
        main_page.click_account_button()
        main_page.set_auth_form(user_email, user_password)
        main_page.click_lk_in_the_header()
        lk_page = LkPage(driver)
        actual_url = lk_page.wait_for_correct_current_url(Urls.LK_PROFILE_URL)
        ApiShop.delete_user(headers)

        assert actual_url == Urls.LK_PROFILE_URL

    @allure.title('Проверка перехода в Историю заказов')
    def test_history_button(self, driver):
        body = GenerationData.create_valid_user_body()
        create_response = ApiShop.create_user(body)
        user_email = create_response.json()['user']['email']
        user_password = body['password']
        headers = GenerationData.get_auth_token_and_create_headers(create_response)
        main_page = MainPage(driver)
        main_page.click_account_button()
        main_page.set_auth_form(user_email, user_password)
        main_page.click_lk_in_the_header()
        lk_page = LkPage(driver)
        lk_page.click_order_history()
        actual_url = lk_page.wait_for_correct_current_url(Urls.ORDER_HISTORY_URL)
        ApiShop.delete_user(headers)

        assert actual_url == Urls.ORDER_HISTORY_URL

    @allure.title('Проверка выхода из аккаунта')
    def test_logout_button(self, driver):
        body = GenerationData.create_valid_user_body()
        create_response = ApiShop.create_user(body)
        user_email = create_response.json()['user']['email']
        user_password = body['password']
        headers = GenerationData.get_auth_token_and_create_headers(create_response)
        main_page = MainPage(driver)
        main_page.click_account_button()
        main_page.set_auth_form(user_email, user_password)
        main_page.click_lk_in_the_header()
        lk_page = LkPage(driver)
        lk_page.click_logout_button()
        actual_url = lk_page.wait_for_correct_current_url(Urls.LOGIN_URL)
        ApiShop.delete_user(headers)

        assert actual_url == Urls.LOGIN_URL
