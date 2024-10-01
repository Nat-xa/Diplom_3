import allure


from pages.main_page import MainPage
from settings import Settings


class TestMainPage:
    @allure.title('Проверка перехода по клику на "Конструктор"')
    def test_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_feed()
        element = main_page.click_constructor()

        assert element.is_displayed

    @allure.title('Проверка перехода по клику на "Лента Заказов"')
    def test_order_feed(self, driver):
        main_page = MainPage(driver)
        element = main_page.click_order_feed()

        assert element.is_displayed

    @allure.title('Проверка появления модального окна по клику на ингредиент')
    def test_open_modal_window_details(self, driver):
        main_page = MainPage(driver)
        main_page.click_constructor()
        modal_window_details = main_page.click_bread_element()

        assert modal_window_details.text == Settings.NAME_BREAD_ELEMENT

    @allure.title('Проверка закрытия модального окна деталей ингредиента по клику на "крестик"')
    def test_close_window_detail(self, driver):
        main_page = MainPage(driver)
        main_page.click_constructor()
        main_page.click_bread_element()
        element = main_page.click_close_button_modal_window_details()

        assert element.is_displayed

    @allure.title('Проверка увеличения каунтера ингредиента при добалении элемента в заказ')
    def test_counter(self, driver):
        main_page = MainPage(driver)
        main_page.click_constructor()
        main_page.click_section_sauces_and_add_sauce_to_order(driver)
        counter_ingredient = main_page.wait_counter_ingredient()
        assert counter_ingredient.text == '1'

    @allure.title('Проверка возможности оформить заказ под авторизованным пользователем')
    def test_set_order_auth_user(self, driver, user_info):
        main_page = MainPage(driver)
        main_page.click_account_button()
        main_page.set_auth_form(user_info[0], user_info[1])
        main_page.add_bread_to_order(driver)
        main_page.click_section_sauces_and_add_sauce_to_order(driver)
        modal_window_id_order = main_page.click_set_order_button()

        assert modal_window_id_order.is_displayed
        