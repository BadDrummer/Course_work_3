from utils import mask_card


def test_mask_card():
    assert mask_card("Visa Classic 6831982476737658") == 'Visa Classic 6831 98** **** 7658'
    assert mask_card("Счет 35383033474447895560") == "Счет **5560"
