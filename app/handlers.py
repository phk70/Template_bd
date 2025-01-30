from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def start_cmd(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name}.')