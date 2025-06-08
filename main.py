import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import CommandStart

# ⛔ Замените на ваш настоящий токен!
BOT_TOKEN = "7824909112:AAHyjZEnTRXpfgawT0wM3LsVbdDRqT8U0Vg"

# Ссылка на старт mini-app (откроется полноэкранно)
STARTAPP_LINK = "https://t.me/SpiritGuide1WIN_bot?startapp=direct"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_handler(message: types.Message):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔮 Открыть Приложение", url=STARTAPP_LINK)]
    ])
    await message.answer("Нажми кнопку ниже, чтобы открыть мини-приложение 👇", reply_markup=kb)

async def main():
    print("Бот запущен.")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
