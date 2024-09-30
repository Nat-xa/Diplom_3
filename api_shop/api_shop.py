import requests

from urls import Urls


class ApiShop:

    @staticmethod
    def create_user(body):
        return requests.post(f'{Urls.BASE_URL}{Urls.CREATE_USER_ENDPOINT}', json=body)

    @staticmethod
    def delete_user(header):
        return requests.delete(f'{Urls.BASE_URL}{Urls.DELETE_USER_ENDPOINT}', headers=header)
