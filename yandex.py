import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str, filename: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        # Тут ваша логика
        # Функция может ничего не возвращать
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(self.token)}
        params = {'path': file_path, 'overwrite': 'true'}
        responce = requests.get(upload_url, headers=headers, params=params)
        href = responce.json().get('href')
        responce = requests.put(href, data=open(filename, 'rb'))
        if responce.status_code == 201:
            print('Файл загружен')
        return responce.status_code


# Получить путь к загружаемому файлу и токен от пользователя
path_to_file = 'dishes.txt'
name_of_file = 'dishes.txt'
token = 'AQAAAAAekZYcAADLW0T0fkUJckWehsgTKNr20iA'
uploader = YaUploader(token)
result = uploader.upload(path_to_file, name_of_file)
