import time

import allure

from locators.orders_feed_page_locators import OrdersFeedPageLocators
from pages.base_page import BasePage


class OrdersFeedPage(BasePage):
    @allure.step('Нажатие на элемент Ленты заказов и ожидание модального окна с деталями заказа')
    def click_element_orders_feed_and_wait_window(self):
        element_orders_feed = self.wait_and_find_element(OrdersFeedPageLocators.ELEMENT_ORDERS_FEED)
        element_orders_feed.click()
        window_details_order = self.wait_and_find_element(OrdersFeedPageLocators.WINDOW_DETAILS_ORDER)
        return window_details_order

    @allure.step('Получение количества "Выполнено за все время')
    def get_count_total_all(self):
        time.sleep(2)
        total_all = self.wait_and_find_element(OrdersFeedPageLocators.TOTAL_ALL).text
        return total_all

    @allure.step('Получение информации о заказах в работе')
    def get_orders_in_work(self):
        orders_in_work = self.wait_and_find_element(OrdersFeedPageLocators.ORDER_IN_WORK)
        time.sleep(3)
        return orders_in_work.text

    @allure.step('Получение id заказа из элемента заказа')
    def get_id_order_from_element_feed(self):
        id_order_from_element_feed = self.wait_and_find_element(OrdersFeedPageLocators.ELEMENT_IN_FEED)
        time.sleep(2)
        return id_order_from_element_feed.text

    @allure.step('Получение количества "Выполнено за сегодня"')
    def get_count_total_today(self):
        time.sleep(3)
        total_today = self.wait_and_find_element(OrdersFeedPageLocators.TOTAL_TODAY).text
        return total_today
