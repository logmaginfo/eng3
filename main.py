from dotenv import load_dotenv #pip install python-dotenv
import asyncio
from aiogram import Bot, Dispatcher, types #from aiogram import Router, F, types
from bd.models import async_main
import os

dp = Dispatcher()
load_dotenv()
bot = Bot(token=os.getenv('TOKEN'))
async def main():
    await async_main()

if __name__ == '__main__':

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Off')