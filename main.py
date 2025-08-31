from aiogram import Bot, Dispatcher, types
import asyncio
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message()
async def handle_message(message: types.Message):
    text = message.text

    # Қарапайым фильтр (міндетті түрде "цена" сөзі болуы керек)
    if "цена" in text.lower():
        await bot.send_message(CHANNEL_ID, f"📢 Жаңа хабарлама:\n\n{text}")
        await message.answer("✅ Хабарлама каналға жіберілді")
    else:
        await message.answer("❌ Хабарлама талапқа сай емес")

async def main():
    await dp.start_polling(bot)

asyncio.run(main())
