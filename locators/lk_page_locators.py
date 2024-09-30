from selenium.webdriver.common.by import By


class LkPageLocators:

    ORDER_HISTORY = [By.XPATH, ".//a[@class = 'Account_link__2ETsJ text text_type_main-medium text_color_inactive']"]
    LOGOUT_BUTTON = [By.XPATH, ".//li[@class = 'Account_listItem__35dAP']/button"]
    HISTORY_ELEMENT = [By.XPATH, ".//p[@class = 'text text_type_digits-default']"]
