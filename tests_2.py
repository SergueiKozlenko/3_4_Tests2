import logging
import requests
import unittest
import sys
from main import YandexAPIClient, TOKEN

logging.basicConfig(stream=sys.stderr, level=logging.INFO)


class TestYandexAPIClient(unittest.TestCase):
    def setUp(self):
        self.client = YandexAPIClient(TOKEN)
        self.false_client = YandexAPIClient('')
        self.test_path = 'test_folder'

    def tearDown(self):
        self.client.delete(self.test_path)

    def test_createFolder(self):
        log = logging.getLogger("Test Create Folder")
        log.info(f"Тест на создание папки  на Яндекс Диске.")
        self.assertEqual(self.false_client.put(self.test_path).status_code, 401)
        log.info(f"Пользователь не авторизован. Код соответствует 401.")
        self.assertEqual(self.client.put(self.test_path).status_code, 201)
        log.info(f"Запрос на создание папки '{self.test_path}'. Код ответа соответствует 201.")
        self.assertEqual(requests.get(self.client.URL, params={'path': self.test_path},
                                      headers=self.client.headers).status_code, 200)
        log.info(f"Результат создания папки '{self.test_path}' - папка появилась на Диске. "
                 f"Код ответа соответствует 200.")
        self.assertEqual(self.client.put(self.test_path).status_code, 409)
        log.info(f"Повторный запрос на создание папки - '{self.test_path}' уже существует. "
                 f"Код ответа соответствует 409.")


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    unittest.main()
