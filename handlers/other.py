from aiogram import types, Dispatcher
from create_bot import dp, bot
import json
import string


# @dp.message_handler()
async def echo_send(message: types.Message):
    if message.text.lower() == 'nigga':
        await bot.send_message(chat_id=message.chat.id,
                               text='Такое писать в нашем чате нельзя!')
        await message.delete()


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(echo_send)