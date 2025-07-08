def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер банковской карты по формату: XXXX XX** **** XXXX.

    :param card_number: Номер карты (16 цифр)
    :return: Замаскированный номер карты
    """
    card_str = card_number
    if len(card_str) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр.")

    part1 = card_str[:4]
    part2 = card_str[4:6]
    part3 = "**"
    part4 = "****"
    part5 = card_str[-4:]

    return f"{part1} {part2}{part3} {part4} {part5}"


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер банковского счёта по формату: **XXXX.

    :param account_number: Номер счёта
    :return: Замаскированный номер счёта
    """
    acc_str = account_number
    if len(acc_str) < 4:
        raise ValueError("Номер счёта должен содержать минимум 4 цифры.")

    return f"**{acc_str[-4:]}"
