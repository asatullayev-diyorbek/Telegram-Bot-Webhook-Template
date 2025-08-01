from aiogram.types import Message
from aiogram import Bot

async def handle_start(message: Message, bot: Bot) -> None:
    try:
        await message.delete()
    except:
        pass

    await message.answer("Ishga tayyorman!")