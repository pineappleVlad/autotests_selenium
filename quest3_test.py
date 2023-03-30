from quest3 import auth_yandex_func
from unittest import TestCase

class TestAuthYandex(TestCase):
    def test_login(self):
        login = ''
        password = ''
        result = auth_yandex_func(login, password)
        self.assertNotEqual(result, 'Такого аккаунта нет')

    def test_password(self):
        login = ''
        password = ''
        result = auth_yandex_func(login, password)
        self.assertNotEqual(result, 'Неверный пароль')

    def test_all(self):
        login = ''
        password = ''
        result = auth_yandex_func(login, password)
        self.assertEqual(result, 'Успешная авторизация')
