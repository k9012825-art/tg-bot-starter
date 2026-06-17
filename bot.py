"""Minimal Telegram bot starter — commands, echo, simple user storage."""

import asyncio
import json
import logging
import os
from pathlib import Path

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DATA_FILE = Path(__file__).parent / "data" / "users.json"


def load_users() -> dict:
    if not DATA_FILE.exists():
        return {}
    return json.loads(DATA_FILE.read_text(encoding="utf-8"))


def save_users(users: dict) -> None:
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    DATA_FILE.write_text(json.dumps(users, ensure_ascii=False, indent=2), encoding="utf-8")


def remember_user(message: Message) -> None:
    users = load_users()
    uid = str(message.from_user.id)
    users[uid] = {
        "username": message.from_user.username,
        "first_name": message.from_user.first_name,
        "last_seen": message.date.isoformat(),
    }
    save_users(users)


async def main() -> None:
    token = os.environ.get("BOT_TOKEN")
    if not token:
        raise SystemExit("Set BOT_TOKEN env variable. See .env.example")

    bot = Bot(token=token)
    dp = Dispatcher()

    @dp.message(CommandStart())
    async def cmd_start(message: Message) -> None:
        remember_user(message)
        await message.answer(
            "Привет! Я демо-бот для портфолио.\n\n"
            "Команды:\n"
            "/help — список команд\n"
            "/ping — проверка связи\n"
            "/stats — сколько пользователей в базе"
        )

    @dp.message(Command("help"))
    async def cmd_help(message: Message) -> None:
        await message.answer("Команды: /start, /help, /ping, /stats\nЛюбой текст — эхо-ответ.")

    @dp.message(Command("ping"))
    async def cmd_ping(message: Message) -> None:
        await message.answer("pong")

    @dp.message(Command("stats"))
    async def cmd_stats(message: Message) -> None:
        count = len(load_users())
        await message.answer(f"Пользователей в локальной базе: {count}")

    @dp.message(F.text)
    async def echo(message: Message) -> None:
        remember_user(message)
        await message.answer(f"Эхо: {message.text}")

    logger.info("Bot started")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
