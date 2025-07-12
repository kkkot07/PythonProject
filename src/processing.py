from typing import List, Dict
from datetime import datetime

def filter_by_state(data: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    """
    Фильтрует список словарей по значению ключа 'state'.

    :param data: список словарей с операциями
    :param state: значение состояния (по умолчанию 'EXECUTED')
    :return: отфильтрованный список
    """
    return [item for item in data if item.get('state') == state]


def sort_by_date(data: List[Dict], descending: bool = True) -> List[Dict]:
    """
    Сортирует список словарей по ключу 'date'.

    :param data: список словарей с операциями
    :param descending: порядок сортировки (по убыванию по умолчанию)
    :return: отсортированный список
    """
    return sorted(data, key=lambda x: datetime.fromisoformat(x['date']), reverse=descending)
