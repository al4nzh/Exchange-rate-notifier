import asyncio
from telegram import Bot
import logging

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
BOT_TOKEN = '6371239450:AAEA78ktq6JEmuXvNnsUO4f7cqjEq7YDe4s'

async def get_chat_id():
    bot = Bot(token=BOT_TOKEN)
    updates = await bot.get_updates()
    if updates:
        chat_id = updates[-1].message.chat.id
        print(f"Chat ID: {chat_id}")
    else:
        print("No updates found")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_chat_id())
    loop.close()

