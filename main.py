import requests

TOKEN = 'AgAAAAAAauhpAADLW5sPOCAL5EKWuK-yLjkuIIU'


class YandexAPIClient:
    URL = 'https://cloud-api.yandex.net/v1/disk/resources'
    TOKEN = ''

    def __init__(self, TOKEN):
        """Конструктор класса YandexAPIClient"""
        self.token = TOKEN
        self.headers = {'Authorization': f'OAuth {self.token}'}

    def get(self, path):
        return requests.get(self.URL, params={'path': path}, headers=self.headers)

    def delete(self, path):
        return requests.delete(self.URL, params={'path': path}, headers=self.headers)

    def put(self, path):
        response = requests.put(self.URL, params={'path': path}, headers=self.headers)
        return response


if __name__ == '__main__':
    client = YandexAPIClient(TOKEN)
    client.put('TEST_folder')
    client.delete('TEST_folder')
