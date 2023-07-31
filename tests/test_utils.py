from utils import mask_card, format_date, filter_data_by_executed, get_all_operations, formatted_data


def test_mask_card():
    assert mask_card("Visa Classic 6831982476737658") == 'Visa Classic 6831 98** **** 7658'
    assert mask_card("Счет 35383033474447895560") == "Счет **5560"


def test_formate_data():
    assert format_date("2019-04-04T23:20:05.206878") == "04.04.2019"


def test_filter_data_by_executed():
    data_for_test = [
        {
            'id': 1,
            'state': 'EXECUTED'
        },
        {
            'id': 2,
            'state': 'CANCELED'
        },
        {
            'id': 3,
            'state': 'EXECUTED'
        }
    ]
    expected_response = [
        {
            'id': 1,
            'state': 'EXECUTED'
        },
        {
            'id': 3,
            'state': 'EXECUTED'
        }
    ]
    assert filter_data_by_executed(data_for_test) == expected_response


def test_formatted_data():
    data_for_test = {
     "id": 441945886,
     "date": "2019-08-26T10:50:58.294041",
     "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
     },
     "description": "Перевод организации",
     "from": "Maestro 1596837868705199",
     "to": "Счет 64686473678894779589"
    }
    expected_response = ('26.08.2019 Перевод организации\n'
 'Maestro 1596 83** **** 5199 -> Счет **9589\n'
 '31957.58 руб.\n')
    assert formatted_data(data_for_test) == expected_response


# def test_get_all_operations():
#     assert type(get_all_operations()) == str
