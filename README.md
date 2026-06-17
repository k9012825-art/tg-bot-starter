# tg-bot-starter

простая база под телеграм-бота. aiogram 3, без лишнего.

## запуск

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
python bot.py
```

токен берёшь у @BotFather, кладёшь в `.env` как `BOT_TOKEN=...`

## что внутри

- /start /help /ping /stats
- эхо на текст
- юзеры пишутся в data/users.json

норм как старт под заказ — дальше докручиваешь под тз
