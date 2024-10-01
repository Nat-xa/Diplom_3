import allure

from pages.lk_page import LkPage
from pages.main_page import MainPage
from urls import Urls


class TestLkPage:

    @allure.title('Проверка перехода по клику на "Личный Кабинет"')
    def test_lk_button(self, driver, user_info):
        main_page = MainPage(driver)
        main_page.click_account_button()
        main_page.set_auth_form(user_info[0], user_info[1])
        main_page.click_lk_in_the_header()
        lk_page = LkPage(driver)
        actual_url = lk_page.wait_for_correct_current_url(Urls.LK_PROFILE_URL)

        assert actual_url == Urls.LK_PROFILE_URL

    @allure.title('Проверка перехода в Историю заказов')
    def test_history_button(self, driver, user_info):
        main_page = MainPage(driver)
        main_page.click_account_button()
        main_page.set_auth_form(user_info[0], user_info[1])
        main_page.click_lk_in_the_header()
        lk_page = LkPage(driver)
        lk_page.click_order_history()
        actual_url = lk_page.wait_for_correct_current_url(Urls.ORDER_HISTORY_URL)

        assert actual_url == Urls.ORDER_HISTORY_URL

    @allure.title('Проверка выхода из аккаунта')
    def test_logout_button(self, driver, user_info):
        main_page = MainPage(driver)
        main_page.click_account_button()
        main_page.set_auth_form(user_info[0], user_info[1])
        main_page.click_lk_in_the_header()
        lk_page = LkPage(driver)
        lk_page.click_logout_button()
        actual_url = lk_page.wait_for_correct_current_url(Urls.LOGIN_URL)

        assert actual_url == Urls.LOGIN_URL
