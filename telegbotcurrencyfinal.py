from bs4 import BeautifulSoup
import requests
from telegram import Bot
from telegram.constants import ParseMode
from telegram.ext import CallbackContext

import time
import asyncio


BOT_TOKEN = '6371239450:AAEA78ktq6JEmuXvNnsUO4f7cqjEq7YDe4s'

CHAT_ID = '458838320'

async def get_currency(in_currency, out_currency):
    url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1'
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    currency = soup.find("span", class_="ccOutputRslt").get_text()
    return currency

async def send_currency_notification():
    in_currency = 'USD'
    out_currency = 'KZT'

    currency_rate = await get_currency(in_currency, out_currency)

    # Create a bot instance and send a notification with the currency exchange rate to Telegram
    bot = Bot(token=BOT_TOKEN)
    notification_message = f"1 {in_currency} = {currency_rate} {out_currency}"
    await bot.send_message(chat_id=CHAT_ID, text=notification_message, parse_mode=ParseMode.MARKDOWN)

async def main():
    while True:
        await send_currency_notification()
        await asyncio.sleep(60)  # Wait for one minute 

if __name__ == "__main__":
    asyncio.run(main())
