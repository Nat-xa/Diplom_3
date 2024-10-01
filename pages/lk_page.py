import allure

from locators.lk_page_locators import LkPageLocators
from pages.base_page import BasePage


class LkPage(BasePage):
    @allure.step('Нажатие на кнопку "История заказов" в личном кабинете')
    def click_order_history(self):
        self.wait_and_find_element(LkPageLocators.ORDER_HISTORY)
        order_history = self.wait_clickable_element(LkPageLocators.ORDER_HISTORY)
        order_history.click()

    @allure.step('Нажатие на кнопку "Выход" в личном кабинете')
    def click_logout_button(self):
        self.wait_and_find_element(LkPageLocators.LOGOUT_BUTTON)
        logout_button = self.wait_clickable_element(LkPageLocators.LOGOUT_BUTTON)
        logout_button.click()

    @allure.step('Получение элемента (заказа) из Истории заказов')
    def get_history_element(self):
        history_element = self.wait_and_find_element(LkPageLocators.HISTORY_ELEMENT)
        return history_element.text
