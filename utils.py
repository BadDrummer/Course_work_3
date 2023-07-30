import json

'''функция для получения исходных данных из json файла'''


def get_all_operations():
    with open("operations.json", encoding='utf-8') as file:
        data = json.load(file)
    return data


'''функция, которая выбирает из исходных данных операции, у которых state = executed'''


def filter_data_by_executed(operations: list):
    result = []
    for operation in operations:
        state = operation.get('state')
        if state and state.lower() == 'executed':
            result.append(operation)
    return result


'''функция для маскировки номера карты или счёта'''


def mask_card(card: str):
    card = card.split(' ')
    if card[0].lower() == 'счет':
        return f'{card[0]} **{card[-1][-4:]}'
    return f'{" ".join(card[:-1])} {card[-1][:4]} {card[-1][4:6]}** **** {card[-1][-4:]}'

