import allure
import pytest
from selenium import webdriver

from api_shop.api_shop import ApiShop
from helpers.generation_data import GenerationData
from urls import Urls


@pytest.fixture(params=['firefox', 'chrome'])
@allure.title('Запуск браузера, закрытие браузера')
def driver(request):
    browser = None
    if request.param == 'firefox':
        browser = webdriver.Firefox()
        browser.maximize_window()
    elif request.param == 'chrome':
        browser = webdriver.Chrome()
        browser.maximize_window()
    browser.get(Urls.BASE_URL)

    yield browser

    browser.quit()


@pytest.fixture(scope='function')
@allure.title('Создание нового пользователя, получение email и пароля, удаление пользователя')
def user_info():
    user_info = []
    body = GenerationData.create_valid_user_body()
    create_response = ApiShop.create_user(body)
    user_email = create_response.json()['user']['email']
    user_info.append(user_email)
    user_password = body['password']
    user_info.append(user_password)
    headers = GenerationData.get_auth_token_and_create_headers(create_response)

    yield user_info

    ApiShop.delete_user(headers)
