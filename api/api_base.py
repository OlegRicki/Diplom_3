import allure
import requests
from constants import Constants

constants = Constants()


class ApiBase:

    @allure.step('Создать нового пользователя по api')
    def create_new_user(self, username: str, email: str, password: str):
        url = constants.BASE_API_URL + 'auth/register'
        response = requests.post(url, json={'email': email, 'password': password, 'name': username})
        if response.status_code == 200:
            return email, password, response.json().get('accessToken')
        else:
            raise Exception(response.status_code, response.text)
    @allure.step('Удалить пользователя по api')
    def delete_user(self, access_token: str):
        url = constants.BASE_API_URL + 'auth/user'

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"{access_token}"
        }

        response = requests.delete(url, headers=headers)

        if response.status_code == 202:
            pass
        else:
            raise Exception(response.status_code, response.text)

    @allure.step('Получить данные ингридиента по api')
    def get_data_ingredients(self):
        url = constants.BASE_API_URL + 'ingredients'
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(response.json())

    @allure.step('Получить id ингридиента по api')
    def get_id_ingredient_from_ingredients_by_name(self, ingredients, name_ingredient: str) -> str:
        ingredients = ingredients['data']
        for ingredient in ingredients:
            if ingredient['name'] == name_ingredient:
                return ingredient['_id']

    @allure.step('Создать заказ пол api')
    def create_order_authorization_user(self, access_token: str):

        ingredients = self.get_data_ingredients()
        bun = self.get_id_ingredient_from_ingredients_by_name(
            ingredients, name_ingredient='Краторная булка N-200i')
        sauce = self.get_id_ingredient_from_ingredients_by_name(
            ingredients, name_ingredient='Соус Spicy-x')
        main = self.get_id_ingredient_from_ingredients_by_name(
            ingredients, name_ingredient='Говяжий метеорит (отбивная)')

        url = constants.BASE_API_URL + 'orders'

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"{access_token}"
        }
        json_data = {'ingredients': [bun, sauce, main]}
        response = requests.post(url, json=json_data, headers=headers)
        if response.status_code == 200:
            return response.json()['order']['number']
        else:
            raise Exception(response.status_code, response.text)

    @allure.step('Отправить запрос на авторизацию пользователя')
    def login(self, login: str, password: str):
        url = constants.BASE_API_URL + 'auth/login'
        response = requests.post(url, json={'email': login, 'password': password})
        return response