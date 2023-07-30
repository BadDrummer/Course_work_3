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


'''функция, которая переводит дату транзакции в требуемый формат ЧЧ.ММ.ГГГГ'''


def format_date(str_date: str) -> str:
    list_date = str_date[:10].split('-')
    return '.'.join(reversed(list_date))


'''функция для вывода данных в требуемом по заданию формате'''


def formatted_data(item: dict):
    item_date = format_date(item.get("date"))

    if item.get("from"):
        from_bill = mask_card(item.get("from")) + ' '
    else:
        from_bill = ''

    to_bill = mask_card(item.get("to"))

    return f'{item_date} {item.get("description")}\n' \
           f'{from_bill}-> {to_bill}\n' \
           f'{item["operationAmount"]["amount"]} {item["operationAmount"]["currency"]["name"]}\n'
