from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(info: str) -> str:
    """
    Маскирует номер карты или счета, включая его тип (например, Visa, Maestro или 'Счет').

    :param info: строка вида 'Visa Classic 7000792289606361' или 'Счет 73654108430135874305'
    :return: строка с замаскированным номером
    """
    parts = info.strip().split()

    if parts[0] == "Счет":
        number = parts[1]
        masked = get_mask_account(number)
        return f"Счет {masked}"
    else:
        number = parts[-1]
        name = " ".join(parts[:-1])
        masked = get_mask_card_number(number)
        return f"{name} {masked}"


def get_date(date_str: str) -> str:
    """
    Преобразует ISO-дату (например, '2024-03-11T02:26:18.671407') в формат ДД.ММ.ГГГГ.

    :param date_str: строка в ISO-формате
    :return: строка в формате 'дд.мм.гггг'
    """
    dt = datetime.fromisoformat(date_str)
    return dt.strftime("%d.%m.%Y")
