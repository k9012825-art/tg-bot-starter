# простой тг-бот, стартовая база под заказы
import asyncio
import json
import os
from pathlib import Path

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise SystemExit("нет BOT_TOKEN — скопируй .env.example в .env")

USERS_FILE = Path(__file__).parent / "data" / "users.json"
bot = Bot(TOKEN)
dp = Dispatcher()


def load_users():
    if not USERS_FILE.exists():
        return {}
    return json.loads(USERS_FILE.read_text(encoding="utf-8"))


def save_users(data):
    USERS_FILE.parent.mkdir(exist_ok=True)
    USERS_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def save_user(msg: Message):
    users = load_users()
    uid = str(msg.from_user.id)
    users[uid] = {
        "name": msg.from_user.first_name,
        "username": msg.from_user.username,
        "last_seen": msg.date.isoformat(),
    }
    save_users(users)


@dp.message(CommandStart())
async def start(msg: Message):
    save_user(msg)
    await msg.answer(
        "привет\n\n"
        "/help — что умею\n"
        "/ping — жив ли бот\n"
        "/stats — сколько юзеров в базе"
    )


@dp.message(Command("help"))
async def help_cmd(msg: Message):
    await msg.answer("команды: /start /help /ping /stats\nлюбой текст — отвечу эхом")


@dp.message(Command("ping"))
async def ping(msg: Message):
    await msg.answer("pong")


@dp.message(Command("stats"))
async def stats(msg: Message):
    n = len(load_users())
    await msg.answer(f"юзеров в базе: {n}")


@dp.message(F.text)
async def echo(msg: Message):
    save_user(msg)
    await msg.answer(f"ты написал: {msg.text}")


async def main():
    print("бот запущен")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
