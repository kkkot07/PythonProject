import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize(
    "number, expected",
    [
        ("1234567812345678", "1234 56** **** 5678"),
        ("7000792289606361", "7000 79** **** 6361"),
    ],
)
def test_get_mask_card_number_valid(number, expected):
    assert get_mask_card_number(number) == expected


def test_get_mask_card_number_invalid_length():
    with pytest.raises(ValueError):
        get_mask_card_number("12345")   # слишком короткий номер


@pytest.mark.parametrize(
    "number, expected",
    [
        ("1234567890", "**7890"),
        ("73654108430135874305", "**4305"),
    ],
)
def test_get_mask_account_valid(number, expected):
    assert get_mask_account(number) == expected


def test_get_mask_account_invalid_length():
    with pytest.raises(ValueError):
        get_mask_account("12")  # меньше 4 символов
