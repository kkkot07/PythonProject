# PythonProject

## Описание проекта

Проект предназначен для обработки данных о банковских операциях клиента.  
Реализованы функции:
- `filter_by_state` — фильтрация по статусу выполнения (`EXECUTED`, `CANCELED` и др.)
- `sort_by_date` — сортировка по дате операций (по убыванию или возрастанию)

---

##  Установка

1. Склонируйте репозиторий:
```bash
git clone git@github.com:kkkot07/PythonProject.git
cd PythonProject
```

2. Создайте виртуальное окружение и активируйте его:
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

3. Установите зависимости с помощью Poetry:
```bash
poetry install
```

Если не используете Poetry:
```bash
pip install -r requirements.txt
```

---

## Запуск и проверка

Запуск тестов:
```bash
pytest
```

Проверка кода:
```bash
flake8 src
mypy src
```

---

## Примеры использования

```python
from src.processing import filter_by_state, sort_by_date

data = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
]

# Фильтрация по умолчанию (только 'EXECUTED')
print(filter_by_state(data))

# Фильтрация по другому статусу
print(filter_by_state(data, state='CANCELED'))

# Сортировка по убыванию (по умолчанию)
print(sort_by_date(data))

# Сортировка по возрастанию
print(sort_by_date(data, reverse=False))
```

---

## Требования

- Python 3.10+
- Poetry (если используется `pyproject.toml`)
