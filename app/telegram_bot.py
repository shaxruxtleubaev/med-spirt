import telegram
from .models import Client
from src.settings.base import (
    TELEGRAM_BOT_TOKEN,
    TELEGRAM_CHAT_ID
)

bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)

async def send_data_to_telegram(data):
    # message = f"Новый клиент:\n\nИмя фамилия: {data['fullname']}\nНомер телефона: {data['phone_number']}"
    message = f"Новый клиент:\n\nИмя фамилия: {data['fullname']}\nНомер телефона: {data['phone_number']}"
    chat_id = TELEGRAM_CHAT_ID
    await bot.send_message(chat_id=chat_id, text=message)