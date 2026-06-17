# tg-bot-starter

Минимальный стартовый Telegram-бот на **Python + aiogram 3**.

Подходит как база для заказов: команды, эхо, локальное хранение пользователей, готов к расширению (админка, уведомления, интеграции).

## Возможности

- `/start`, `/help`, `/ping`, `/stats`
- Эхо на любой текст
- Сохранение пользователей в `data/users.json`

## Быстрый старт

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
pip install -r requirements.txt
copy .env.example .env        # вставь токен от @BotFather
python bot.py
```

## Переменные окружения

| Переменная | Описание |
|------------|----------|
| `BOT_TOKEN` | Токен бота от [@BotFather](https://t.me/BotFather) |

## Стек

- Python 3.12+
- [aiogram 3](https://docs.aiogram.dev/)

## Лицензия

MIT — свободно использовать в коммерческих проектах.
