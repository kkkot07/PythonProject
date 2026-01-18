import pytest


@pytest.fixture
def card_number_valid():
    return "7000792289606361"


@pytest.fixture
def account_number_valid():
    return "73654108430135874305"


@pytest.fixture
def operations_list():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-04-12T12:00:00"},
        {"id": 2, "state": "CANCELED", "date": "2023-01-10T10:00:00"},
        {"id": 3, "state": "EXECUTED", "date": "2022-12-01T09:00:00"},
        {"id": 4, "state": "PENDING", "date": "2023-05-20T08:00:00"},
    ]
