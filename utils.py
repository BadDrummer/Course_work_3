import json

'''функция для получения исходных данных из json файла'''


def get_all_operations():
    with open("operations.json", encoding='utf-8') as file:
        data = json.load(file)
    return data
