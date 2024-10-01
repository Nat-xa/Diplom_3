import allure
import requests

from urls import Urls


class ApiShop:

    @staticmethod
    @allure.title('Запрос для создания нового пользователя')
    def create_user(body):
        return requests.post(f'{Urls.BASE_URL}{Urls.CREATE_USER_ENDPOINT}', json=body)

    @staticmethod
    @allure.title('Запрос для удаления пользователя')
    def delete_user(header):
        return requests.delete(f'{Urls.BASE_URL}{Urls.DELETE_USER_ENDPOINT}', headers=header)
