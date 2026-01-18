import pytest
from src.widget import mask_account_card, get_date


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("Visa Classic 7000792289606361", "Visa Classic 7000 79** **** 6361"),
        ("MasterCard 1234567812345678", "MasterCard 1234 56** **** 5678"),
    ],
)
def test_mask_account_card_for_cards(input_str, expected):
    assert mask_account_card(input_str) == expected


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Счет 123456789", "Счет **6789"),
    ],
)
def test_mask_account_card_for_accounts(input_str, expected):
    assert mask_account_card(input_str) == expected


def test_mask_account_card_invalid_format():
    with pytest.raises(ValueError):
        mask_account_card("Visa")  # нет номера карты


@pytest.mark.parametrize(
    "iso, expected",
    [
        ("2023-04-12T12:00:00", "12.04.2023"),
        ("2022-01-01T00:00:00", "01.01.2022"),
    ],
)
def test_get_date(iso, expected):
    assert get_date(iso) == expected
