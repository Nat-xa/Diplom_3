import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Нахождение элемента')
    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 40).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Ожидание кликабельности элемента')
    def wait_clickable_element(self, locator):
        WebDriverWait(self.driver, 40).until(expected_conditions.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)

    @allure.step('Ожидание URL')
    def wait_for_correct_current_url(self, desired_url):
        WebDriverWait(self.driver, 40).until(expected_conditions.url_to_be(desired_url))
        return self.driver.current_url

    @allure.step('Перетаскивание элемента')
    def drag_and_drop_element(self, driver, locator_1, locator_2):
        action = ActionChains(driver)
        action.drag_and_drop(locator_1, locator_2).perform()
