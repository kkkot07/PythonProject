import pytest
from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_default(operations_list):
    result = filter_by_state(operations_list)
    assert len(result) == 2
    assert all(op["state"] == "EXECUTED" for op in result)


@pytest.mark.parametrize("state, expected_count", [
    ("EXECUTED", 2),
    ("CANCELED", 1),
    ("PENDING", 1),
    ("UNKNOWN", 0),
])
def test_filter_by_state_param(operations_list, state, expected_count):
    result = filter_by_state(operations_list, state)
    assert len(result) == expected_count


def test_sort_by_date_descending(operations_list):
    sorted_list = sort_by_date(operations_list)
    dates = [op["date"] for op in sorted_list]
    assert dates == sorted(dates, reverse=True)


def test_sort_by_date_ascending(operations_list):
    sorted_list = sort_by_date(operations_list, descending=False)
    dates = [op["date"] for op in sorted_list]
    assert dates == sorted(dates)
