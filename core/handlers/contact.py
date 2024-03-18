from aiogram.types import Message
from aiogram import Bot



async def get_true_contact(message: Message, bot: Bot):
    if message.contact.user_id == message.from_user.id:
        await message.answer(f"no'mer to'g'ri{message.contact.phone_number}")
    else:
        await message.answer(f"no'mer noto'g'ri")




