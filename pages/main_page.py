import time

import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Нажатие на кнопку "Войти в аккаунт"')
    def click_account_button(self):
        account_button = self.wait_and_find_element(MainPageLocators.ACCOUNT_BUTTON)
        time.sleep(3)
        account_button.click()

    @allure.step('Нажатие на "Личный Кабинет"')
    def click_lk_in_the_header(self):
        lk = self.wait_and_find_element(MainPageLocators.LK_IN_THE_HEADER)
        time.sleep(2)
        lk.click()

    @allure.step('Нажатие на кнопку "Восстановить пароль"')
    def click_password_recovery_button(self):
        password_recovery_button = self.wait_and_find_element(MainPageLocators.PASSWORD_RECOVERY_BUTTON)
        password_recovery_button.click()

    @allure.step('Заполнение поля Email в форме авторизации')
    def set_email_login(self, email):
        email_login = self.wait_and_find_element(MainPageLocators.EMAIL_LOGIN)
        email_login.send_keys(email)

    @allure.step('Заполнение поля "Пароль" в форме авторизации')
    def set_password_login(self, password):
        password_login = self.wait_and_find_element(MainPageLocators.PASSWORD_LOGIN)
        password_login.send_keys(password)

    @allure.step('Нажатие на кнопку "Войти" в форме авторизации')
    def click_login_button(self):
        login_button = self.wait_and_find_element(MainPageLocators.LOGIN_BUTTON)
        login_button.click()

    @allure.step('Заполнение полей формы авторизации и нажатие на кнопку "Войти"')
    def set_auth_form(self, email, password):
        self.set_email_login(email)
        self.set_password_login(password)
        self.click_login_button()

    @allure.step('Нажатие на "Конструктор"')
    def click_constructor(self):
        constructor = self.wait_and_find_element(MainPageLocators.CONSTRUCTOR)
        time.sleep(2)
        constructor.click()
        element = self.wait_and_find_element(MainPageLocators.CONSTRUCTOR_ACTIV)
        return element

    @allure.step('Нажатие на "Лента Заказов"')
    def click_order_feed(self):
        constructor = self.wait_and_find_element(MainPageLocators.ORDER_FEED)
        time.sleep(2)
        constructor.click()
        element = self.wait_and_find_element(MainPageLocators.ORDER_FEED_ACTIV)
        return element

    @allure.step('Нажатие на ингредиент')
    def click_bread_element(self):
        element_bread = self.wait_and_find_element(MainPageLocators.ELEMENT_BREAD)
        element_bread.click()
        modal_window_details = self.wait_and_find_element(MainPageLocators.MODAL_WINDOW_DETAILS)
        return modal_window_details

    @allure.step('Нажатие на "крестик" в модальном окне деталей ингредиента')
    def click_close_button_modal_window_details(self):
        close_button = self.wait_and_find_element(MainPageLocators.CLOSE_WINDOW_DETAILS)
        time.sleep(3)
        close_button.click()
        element = self.wait_and_find_element(MainPageLocators.AFTER_CLOSE_WINDOW_DETAILS)
        return element

    @allure.step('Нажатие на раздел "Соусы" и добавление соуса в корзину')
    def click_section_sauces_and_add_sauce_to_order(self, driver):
        section_sauces = self.wait_and_find_element(MainPageLocators.SECTION_SAUCES)
        time.sleep(2)
        section_sauces.click()
        sauce = self.wait_and_find_element(MainPageLocators.ELEMENT_SAUCES)
        basket = self.wait_and_find_element(MainPageLocators.BASKET)
        self.drag_and_drop_element(driver, locator_1=sauce, locator_2=basket)

    @allure.step('Ожидание изменения счетчика в ингредиенте')
    def wait_counter_ingredient(self):
        counter_ingredient = self.wait_and_find_element(MainPageLocators.COUNTER_INGREDIENT)
        time.sleep(3)
        return counter_ingredient

    @allure.step('Добавление булочки в заказ')
    def add_bread_to_order(self, driver):
        bread = self.wait_and_find_element(MainPageLocators.ELEMENT_BREAD)
        basket = self.wait_and_find_element(MainPageLocators.BASKET)
        self.drag_and_drop_element(driver, locator_1=bread, locator_2=basket)

    @allure.step('Нажатие на кнопку "Оформить заказ"')
    def click_set_order_button(self):
        order_button = self.wait_and_find_element(MainPageLocators.SET_ORDER_BUTTON)
        order_button.click()
        modal_window_id_order = self.wait_and_find_element(MainPageLocators.MODAL_WINDOW_ID_ORDER)
        return modal_window_id_order

    @allure.step('Нажатие на "крестик" в модальном окне деталей заказа')
    def click_close_button_modal_window_id_order(self):
        close_button = self.wait_and_find_element(MainPageLocators.MODAL_WINDOW_ID_ORDER_CLOSE)
        time.sleep(2)
        close_button.click()

    @allure.step('Получение id заказа из модального окна после оформления заказа')
    def get_id_order(self):
        id_order = self.wait_and_find_element(MainPageLocators.ID_ORDER).text
        return f'0{id_order}'

    @allure.step('Переход в Конструктор и создание заказа')
    def create_order(self, driver):
        self.click_constructor()
        self.add_bread_to_order(driver)
        self.click_section_sauces_and_add_sauce_to_order(driver)
        self.click_set_order_button()
