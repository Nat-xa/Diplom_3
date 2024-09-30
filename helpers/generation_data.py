import random

from settings import Settings


class GenerationData:

    @staticmethod
    def generate_valid_email():
        return f"natali_dmitrievsky_1274_{random.randint(100, 999)}@yandex.ru"

    @staticmethod
    def generate_valid_password():
        return f"F{random.randint(10, 99)}-{random.randint(10, 99)}"

    @staticmethod
    def create_valid_user_body():
        email = GenerationData.generate_valid_email()
        password = GenerationData.generate_valid_password()
        body = {
            "email": email,
            "password": password,
            "name": Settings.USER_NAME
        }
        return body

    @staticmethod
    def get_auth_token_and_create_headers(response):
        user_token = response.json()['accessToken']
        headers = {'Authorization': f'{user_token}'}
        return headers
