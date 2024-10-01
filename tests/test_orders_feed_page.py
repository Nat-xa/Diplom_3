import allure


from pages.lk_page import LkPage
from pages.main_page import MainPage
from pages.orders_feed_page import OrdersFeedPage


class TestOrdersFeedPage:

    @allure.title('Проверка открытия модального окна при клике на заказ')
    def test_window_details_order(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_feed()
        order_feed_page = OrdersFeedPage(driver)
        element = order_feed_page.click_element_orders_feed_and_wait_window()

        assert element.is_displayed

    @allure.title('Проверка увеличения счетчика "Выполнено за все время" при создании нового заказа')
    def test_total_all_after_order(self, driver, user_info):
        main_page = MainPage(driver)
        main_page.click_account_button()
        main_page.set_auth_form(user_info[0], user_info[1])
        main_page.click_order_feed()
        order_feed_page = OrdersFeedPage(driver)
        count_total_all = order_feed_page.get_count_total_all()
        main_page = MainPage(driver)
        main_page.click_constructor()
        main_page.add_bread_to_order(driver)
        main_page.click_section_sauces_and_add_sauce_to_order(driver)
        main_page.click_set_order_button()
        main_page.click_close_button_modal_window_id_order()
        main_page.click_order_feed()
        order_feed_page = OrdersFeedPage(driver)
        count_total_all_after_order = order_feed_page.get_count_total_all()

        assert count_total_all_after_order == str((int(count_total_all)) + 1)

    @allure.title('Проверка появления заказа в разделе "В работе" после оформления заказа')
    def test_order_in_work(self, driver, user_info):
        main_page = MainPage(driver)
        main_page.click_account_button()
        main_page.set_auth_form(user_info[0], user_info[1])
        main_page.create_order(driver)
        id_order = main_page.get_id_order()
        main_page.click_close_button_modal_window_id_order()
        main_page.click_order_feed()
        order_feed_page = OrdersFeedPage(driver)
        orders_in_work = order_feed_page.get_orders_in_work()

        assert orders_in_work == id_order

    @allure.title('Проверка отображения заказа пользователя из раздела "История заказов" на странице "Лента Заказов"')
    def test_orders_in_history_and_feed(self, driver, user_info):
        main_page = MainPage(driver)
        main_page.click_account_button()
        main_page.set_auth_form(user_info[0], user_info[1])
        main_page.create_order(driver)
        main_page.click_close_button_modal_window_id_order()
        main_page.click_lk_in_the_header()
        lk_page = LkPage(driver)
        lk_page.click_order_history()
        order_in_history = lk_page.get_history_element()
        main_page = MainPage(driver)
        main_page.click_order_feed()
        orders_feed_page = OrdersFeedPage(driver)
        order_in_feed = orders_feed_page.get_id_order_from_element_feed()

        assert order_in_history == order_in_feed

    @allure.title('Проверка увеличения счетчика "Выполнено за сегодня" при создании нового заказа')
    def test_total_today_after_order(self, driver, user_info):
        main_page = MainPage(driver)
        main_page.click_account_button()
        main_page.set_auth_form(user_info[0], user_info[1])
        main_page.click_order_feed()
        order_feed_page = OrdersFeedPage(driver)
        count_total_today = order_feed_page.get_count_total_today()
        main_page = MainPage(driver)
        main_page.create_order(driver)
        main_page.click_close_button_modal_window_id_order()
        main_page.click_order_feed()
        order_feed_page = OrdersFeedPage(driver)
        count_total_today_after_order = order_feed_page.get_count_total_today()

        assert count_total_today_after_order == str((int(count_total_today)) + 1)
